#!/usr/bin/env python
# fileencoding=utf-8

from tornado_start.options import define, options


def define_app_options():
    define_common_options()

    define('debug', default=True)

    define('with_https', default=False)
    define('cookie_secret', default='<bad secret>')

    define('mongodb_host', default="10.0.0.76")
    define('userdb_name', default="enjoystudy")
    define('db_name')
    define('shiredb_name')

    define('shiredb_host', default="10.0.0.76")

    define('replica_set', default='')
    define('w_value', default=0)
    define('wtimeout', default=5000)

    define('redis_host', default="10.0.0.76")
    define('redis_db', default=1)

    define('port', default=8888)

    define('gemstone_host', '10.0.0.76:7102')
    define('coin_host', '10.0.0.76:7189')
    define('klx_account_host', '127.0.0.1:8133')
    define('scanservice_host', '127.0.0.1:8810')

    define('gen_pdf_host', default='http://10.0.0.98:12345')

    define('passport_host', default='http://passport.kuailexue.com')
    define('https_passport_host', default='https://passport.kuailexue.com')


def define_common_options():
        # 腾讯企业邮箱发送
    define('smtp_host', 'smtp.exmail.qq.com')
    define('smtp_username', 'service-no-reply@kuailexue.com')
    define('smtp_password', 'd04aQchYDJxNcvst')
    define('smtp_realname', u'快乐学')

    # SendCloud发送
    define('sc_api_user', 'service_mail_no_reply'),
    define('sc_api_key', 'el4duT4idM5iE1Bd'),
    define('sc_from', 'service-no-reply@service-mail.kuailexue.com'),
    define('sc_fromname', u'快乐学'),

    define('loggingserver_host', "127.0.0.1")
    define('loggingserver_port', 9020)

    # 文件路径
    define('img_data_path', 'data/img')
    define('doc_data_path', 'data/exam')
    define('audio_data_path', 'data/audio')
    define('video_data_path', 'data/video')
    define('pdf_data_path', 'data/pdf')
    define('pdf_paper_path', 'data/pdf/paper')
    define('paper_docx_path', 'data/paper')
    define('exam_excel_path', 'data/excel')
    define('pdf_fragment_path', 'data/pdf/item')

    # url 路径
    define('img_data_url_prefix', '/data/img/')
    define('audio_data_url_prefix', '/data/audio/')
    define('video_data_url_prefix', '/data/video/')
    define('pdf_data_url_prefix', '/data/pdf/')
    define('paper_docx_url_prefix', '/data/doc/')

    # 下载路径
    define('stu_android', 'http://openapi.kuailexue.com/static/app/kuailexue_student.apk')
    define('stu_ios', 'https://appsto.re/cn/MJB4_.i')
    define('teacher_android', 'http://openapi.kuailexue.com/static/app/kuailexue_teacher.apk')
    define('teacher_ios', 'https://appsto.re/cn/z3FBbb.i')
    define('stu_weixin', 'http://a.app.qq.com/o/simple.jsp?pkgname=com.kuailexue.student')
    define('teacher_weixin', 'http://a.app.qq.com/o/simple.jsp?pkgname=com.kuailexue.teacher')

    define('alipay_mobile_ali_public_key', u'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCnxj/9qwVfgoUh/y2W89L6BkRAFljhNhgPdyPuBV64bfQNN1PjbCzkIM6qRdKBoLPXmKKMiFYnkd6rAoprih3/PrQEB/VsW8OoM8fxn67UDYuyBTqA23MML9q1+ilIZwBC2AQ2UBVOrFXfFl75p6/B5KsiNG9zpgmLCUYuLkxpLQIDAQAB\n-----END PUBLIC KEY-----')  # noqa
    define('alipay_mobile_klx_private_key', u'-----BEGIN PRIVATE KEY-----\nMIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBANAD8bJUjisec9WAIOO7pJATH+885vHBMxRiWhidIaVXlSekMNcWkSD0pYX5ozoGM1naQhEX2cjUJnMscWUnDZwr03M0NIfPeG094dIXseex8aTxyJF6EhWKpxSceLV/xjm7Wu25lqv3BnFQZpbEQ078i76f0d7Bfgf81onfCPSxAgMBAAECgYBzVlyDVqLlgaMUdFDINNjQEeqZChm7XjZmTQpLr4RiWyeWrVFvUVHzBfNpT7uThrCeV4heVe0pj4gqQDA3t+mw974hzz3aWwzXl2wFpdOcsB0V9NzfiHsAiUzyJvEO6RfSsDHk7wE/eptwUrOSPGTUAlSiipXM6gCLSSlBlUw/4QJBAPSJUF/Y6oZ9k8Z5cs0SPOqnoBDzGmDdm6cEOt53X4Eenalzm0R0HZa/9eN91tD8cNsQu6ZsOSORNeCGf/FqSa0CQQDZxFdY3Kq8DtpII4HXUSBN9lo/4PIbrljNzOYV9cwcDiTFNT7dwF/EgTA2XieU/lup9xTYgj0ra4W+x6SahL+VAkBWxzffm6G2cm/zmfu0bIlzmGLEQREWWO44udaORfx9XLkEfkMWasJpUdvXjDukVEFUbD67U2J/jbN55yEWMerNAkA9BEmhKXthZBv/WIuaBC40ChHxkhrkbK6PQ5k4j/2X4tKkuy2ZPrzWt4gFw839bmPKtOOPYra3AtKfyRqy/P0dAkBbabisGqsGly16yko36gdRwJzQWi2bJgllDvmid3IA7GyfuLsDb/4kZlwMxzeOVLYLPg+sFrrrRzkCf7oHaXk8\n-----END PRIVATE KEY-----')  # noqa

    define('partner_aotu_appkey')
    define('partner_aotu_public_key')
    define('partner_aotu_private_key')  # debug
    define('partner_aotu_klx_private_key')
    define('partner_aotu_klx_public_key')
    define('partner_aotu_get_user_info_url')

    define("platform_xxt_key", "*^klx1$%0")
    define("platform_xxt_id", "xxt")
    define("platform_xxt_appid", "klx")
    define("platform_xxt_business_code", "KLX")

    define("platform_yyj_id", "yyj")
    define("platform_yyj_key", "platform")

    define("platform_7day_id", "7day")
    define("platform_7day_key", "[!2:)5.8")

    define("web_root_url", "http://kuailexue.com/")

    # options.add_parse_callback(lambda: AutoPartner.from_options('aotu'))
    # options.add_parse_callback(lambda: QTPartner.from_options('yyj'))
    # options.add_parse_callback(lambda: XXTPartner.from_options('xxt'))
    # options.add_parse_callback(lambda: SevenDayPartner.from_options('7day'))
