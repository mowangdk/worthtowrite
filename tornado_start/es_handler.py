#!/usr/bin/env python
# fileencoding=utf-8
from tornado_start import defines


class Subject(object):
    kSubjectIds = {1, 2, 3, 4, 5}
    Subject_name = ['english', 'math', 'physics', 'chemistry', 'biology']

    def __init__(self, name):
        self.name = name
        self.zh_name = u''
        self.parser = None
        self.common = None
        self.item_class = None
        self.render = None
        self.docx_render = None
        self.site_root = None

    _SUBJECTS = {}

    @classmethod
    def get(cls, val):
        if val in cls._SUBJECTS:
            return cls._SUBJECTS[val]

        if val == 'english' or val == defines.SUBJECT_ENGLISH:
            name = 'english'
            zh_name = u'英语'
            id_ = defines.SUBJECT_ENGLISH
            site_root = u''
        else:
            return None

        subject = Subject(name)
        subject.id_ = id_
        subject.zh_name = zh_name
        subject.site_root = site_root

        cls._SUBJECTS[subject.id_] = subject
        cls._SUBJECTS[subject.name] = subject

        return subject

    @classmethod
    def valid_subject_id(cls, id_):
        return id_ in cls.kSubjectIds

    @classmethod
    def valid_subject_name(cls, id_):
        return id_ in ('english', 'math', 'physics', 'chemistry', 'biology')
