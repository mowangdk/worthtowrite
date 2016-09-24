#!/usr/bin/env python
# fileencoding=utf-8
import logging
import os

import datetime

from concurrent import futures
from jinja2 import FileSystemLoader, Environment, ChoiceLoader
from redis import StrictRedis
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.log import gen_log
from tornado_start.options import parse_command_line, options, parse_config_file
from tornado_start.web import Application

from tornado_start import routes
from tornado_start import settings
from tornado_start.collection_queue import CollectionQueue
from tornado_start.es_handler import Subject
from tornado_start.request_handler import SmartStaticFileHandler, MultiFileFinder
from tornado_start.session import SessionManager

_ALL_SUPPORT_SUBJECTS = ['math', 'physics', 'biology', 'chemistry']

def _ts_format(ts, format=None):
    dt = datetime.datetime.fromtimestamp(ts)
    if format is None:
        return dt.strftime("%m-%d %H:%M")
    elif format == 'absolute':
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    elif format == 'onlydate':
        return dt.strftime('%m-%d')
    elif format == 'fulldate':
        return dt.strftime('%Y-%m-%d')
    elif format == 'ym':
        return dt.strftime(u'%Y年%m月')
    else:
        return dt.strftime(format)


def _num_to_word(num):
    assert isinstance(num, int)
    trans_dict = {
        '1': u'一',
        '2': u'二',
        '3': u'三',
        '4': u'四',
        '5': u'五',
        '6': u'六',
        '7': u'七',
        '8': u'八',
        '9': u'九',
        '0': u'零',
    }
    return u''.join([trans_dict[i] for i in str(num)])


class JinjaLoader(object):

    def __init__(self, **kwargs):
        super(JinjaLoader, self).__init__()
        auto_reload = kwargs.get('debug', True)
        loader = kwargs.get('loader')
        if not loader:
            root_path = kwargs.get('root_path')
            if not loader:
                assert 'no loader could be selected!'
            loader = FileSystemLoader(root_path)
        auto_escape = kwargs.get('auto_escape', guess_autoescape)
        self.env = Environment(loader=loader,
                               autoescape=auto_escape,
                               extensions=['jinja2.ext.autoescape'],
                               trim_blocks=True,
                               lstrip_blocks=True,
                               cache_size=-1,
                               bytecode_cache=MemoryBytecodeCache(),
                               auto_reload=auto_reload)
        additional_globals = {
            'ord': ord,
            'chr': chr,
            'unichr': unichr,
            'json_encode': escape.json_encode
        }

        self.env.globals.update(additional_globals)
        self.env.filters['ts_format'] = _ts_format
        self.env.filters['num_to_word'] = _num_to_word


class EnjoyStudy(Application):

    def __init__(self, options):
        self_dir = os.path.dirname(os.path.abspath(__file__))
        loader = JinjaLoader(loader=ChoiceLoader([
            FileSystemLoader(os.path.join(self_dir, 'templates')),
            FileSystemLoader(os.path.join(self_dir, 'klxlib/templates')),
        ]), debug=options.debug)

        SmartStaticFileHandler.file_finder = MultiFileFinder(
            [os.path.join(self_dir, 'static')],
            os.path.join(self_dir, 'klxlib/static')
        )

        app_settings = dict(
            template_loader=loader,
            static_path=u'/static/',
            static_url_prefix='/klx/static/',
            static_handler_class=SmartStaticFileHandler,
            cookie_secret=options.cookie_secret,
            xsrf_cookies=True,
            login_url="/auth/login",
            debug=options.debug,
        )

        self.name = u"欢乐学习"

        client = self.set_up_db(options.mongodb_host,
                                options.replica_set,
                                w=options.w_value,
                                wtimeout=options.wtimeout)

        self.db_client = client
        self.userdb = client[options.userdb_name]

        self.subjects = {}
        the_routes = routes.get_main_route(options)

        self.default_subject = _ALL_SUPPORT_SUBJECTS[0]
        for subject_name in _ALL_SUPPORT_SUBJECTS:
            self.load_subject_conf(subject_name)
            subject = Subject.get(subject_name)
            the_routes += routes.get(options, subject_name, subject.site_root)

            subject.db = client[options.db_name]
            subject.tc = self.set_up_tc(subject.db)
            subject.queue = CollectionQueue(subject.db, 'queue')
            self.subjects[subject_name] = subject

        self.redis = StrictRedis(options.redis_host, db=options.redis_db, socket_timeout=5.0)

        self.redis.exists('dumb_key_test_connectivity') # force to connect

        self.session_manager = SessionManager(self.redis)

        self.executor = futures.ThreadPoolExecutor(2)

        super(EnjoyStudy, self).__init__(the_routes, **app_settings)


def start(app):
    server = HTTPServer(app, xheaders=True)
    server.listen(options.port)

    if options.with_https:
        assert options.debug
        https_server = HTTPServer(app, xheaders=True, ssl_options={
            'certfile': 'server.crt',
            'keyfile': server.key
        })
        https_server.listen(443)

    install_tornado_shutdown_handler(IOLoop.instance(), server, gen_log)

    IOLoop.instance().start()
    app.executor.shutdown()
    app.db_client.close()
    app.shire_client.close()




def setup_log(options):
    if options.debug:
        pass
    else:
        host = options.loggingserver_host
        port = options.loggingserver_port
        handler = logging.handlers.SocketHandler(host, port)
        handler.closeOnError = 1
        logging.getLogger().addHandler(handler)


def main():
    settings.define_app_options()
    parse_command_line(final=False)
    conf_filename = "server.conf"
    if not options.debug:
        conf_filename = "prod.conf"
    if os.path.exists(conf_filename):
        parse_config_file(conf_filename, final=False)
    else:
        print 'no {} found, skip it'.format(conf_filename)
    parse_command_line(final=True)
    setup_log(options)

    app = EnjoyStudy(options)
    start(app)


if __name__ == '__main__':
    import sys
    sys.exit(main())