#!/usr/bin/env python
#fileencoding=utf-8
from uuid import uuid4

from bson import ObjectId
from tornado.escape import json_decode, json_encode


class Session(object):

    def __init__(self, sid, dict_=None):
        if dict_:
            self.dict_ = dict(dict_)
        else:
            self.dict_ = {}
        self.sid = sid
        self._dirty = False

    def __getitem__(self, key):
        return self.dict_[key]

    def __setitem__(self, key, value):
        self._dirty = True
        self.dict_[key] = value

    def __delitem__(self, key):
        self._dirty = True
        del self.dict_[key]

    _DEFAULT_ARGUMENT = object()

    def get(self, name, default=_DEFAULT_ARGUMENT ):
        if default is self._DEFAULT_ARGUMENT:
            return self.dict_[name]
        else:
            return self.dict_.get(name, default)

    def __contains__(self, key):
        return key in self.dict_

    def __getattr__(self, name):
        try:
            return self.dict_[name]
        except KeyError as ex:
            raise AttributeError(name)

    @property
    def dirty(self):
        return self._dirty

    def json_encode(self):
        return self.dict_

    def __str__(self):
        return "session(sid='{0}', dirty={1}) {2}".format(self.sid, self.dirty, self.dict_)


type_encoders = [(ObjectId, str),]


type_encoders.append((Session, Session.json_encode()))

def uuid_rand():
    '''
    prefer to rand_string
    :return:
    '''
    return uuid4().hex


class SessionManager(object):
    new_session_id = staticmethod(uuid_rand)

    def __init__(self, redis):
        self.redis = redis
        self.expire_time = 3600 * 2
        self.key_prefix = 'session:'

    def new_session(self, sid=None):
        if not sid:
            sid = self.new_session_id()
        session = Session(sid)
        session._dirty = True
        return session

    def open_session(self, sid):
        data = self.redis.get(self.key_prefix + sid)
        if data:
            data = json_decode(data)
            return Session(sid, data)
        else:
            return None

    def save_session(self, session):
        data = json_encode(session)
        self.redis.setex(
            self.key_prefix + session.sid,
            self.expire_time,
            data
        )
        session._dirty = False

    def delete_session_by_token(self, token):
        self.redis.delete(self.key_prefix + token)

    def delete_session(self, user):
        self.redis.delete(
            self.key_prefix + user.login_token
        )

    def set_expire_time(self, expire_time):
        self.expire_time = expire_time
