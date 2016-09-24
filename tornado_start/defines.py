#!/usr/bin/env python
# fileencoding=utf-8

USER_ROLE_ADMIN = 0
USER_ROLE_TEACHER = 1
USER_ROLE_STUDENT = 2
USER_ROLE_PARENT = 3
USER_ROLE_ANONYMITY = 4
USER_ROLE_PARTNER = 5
USER_ROLE_EMPLOYEE = 6
USER_ROLE_SYSTEM = 7
USER_ROLE_MARKETING = 8  # 市场推广后台管理, 包括用户邮箱绑定、重置密码


def user_role_name(role):
    return {
        0: u'管理员',
        1: u'老师',
        2: u'学生',
        3: u'家长',
        4: u'匿名用户',
        5: u'合作伙伴',
        6: u'问答员工',
        7: u'系统',
        8: u'市场',
    }.get(role, u'未知角色')


EXAM_TYPE_SMEE = 3  # 中考
EXAM_TYPE_NCEE = 4  # 高考

# 级段
SCHOOLING_STAGE_KINDERGARTEN = 1  # 幼儿园
SCHOOLING_STAGE_PRIMARY = 2  # 小学
SCHOOLING_STAGE_JUNIOR_MIDDLE = 3  # 初中
SCHOOLING_STAGE_SENIOR_MIDDLE = 4  # 高中
SCHOOLING_STAGE_HIGHER = 5  # 高等教育/大学


def schooling_stage_name(stage):
    return {
        1: u'幼儿园',
        2: u'小学',
        3: u'初中',
        4: u'高中',
        5: u'高等教育',
    }.get(stage, u'未知学段')


# 文理分科
GRADE_CAT_NONE = 0  # 不限
GRADE_CAT_LIBERAL = 1  # 文科
GRADE_CAT_SCIENCE = 2  # 理科


def grade_cat_name(cat):
    return {
        0: u'无',
        1: u'文科',
        2: u'理科'
    }.get(cat, u'未知分科')


def grade_cats_name(cats):
    if not cats:
        return u'无'
    if len(cats) >= 2:
        return u'无'
    return grade_cat_name(cats[0])


SUBJECT_NONE = 0
SUBJECT_ENGLISH = 1
SUBJECT_MATH = 2
SUBJECT_PHYSICS = 3
SUBJECT_CHEMISTRY = 4
SUBJECT_BIOLOGY = 5

SUBJECT_DEFAULT = SUBJECT_ENGLISH


exam_classes = {
    # 0: u'无',
    1: u'高考真题',
    2: u'中考真题',
    3: u'高中多校联考',
    4: u'初中多校联考',
    5: u'重要区县高考模拟题',
    6: u'全国重点初中模拟题',
    7: u'高中习题集',
    8: u'初中习题集',
}


ncee_provinces = [
    u'安徽',
    u'北京',
    u'福建',
    u'甘肃',
    u'贵州',
    u'广东',
    u'广西',
    u'海南',
    u'河北',
    u'河南',
    u'黑龙江',
    u'湖北',
    u'湖南',
    u'吉林',
    u'江苏',
    u'江西',
    u'辽宁',
    u'内蒙古',
    u'宁夏',
    u'青海',
    u'山东',
    u'山西',
    u'陕西',
    u'上海',
    u'四川',
    u'天津',
    u'西藏',
    u'新疆',
    u'云南',
    u'浙江',
    u'重庆',
]

grades = [
    [1, u'一年级'],
    [2, u'二年级'],
    [3, u'三年级'],
    [4, u'四年级'],
    [5, u'五年级'],
    # [6, u'六年级'],
    [6, u'小学组'],
    [7, u'初一'],
    [8, u'初二'],
    [9, u'初三'],
    # [10, u'初四'],
    [11, u'高一'],
    [12, u'高二'],
    [13, u'高三'],
]

KNOWLEDGE_TAG_FREQ_CLASS_HIGH = 10
KNOWLEDGE_TAG_FREQ_CLASS_NORMAL = 5
KNOWLEDGE_TAG_FREQ_CLASS_LOW = 0


PAGE_SIZE_SMALL = 5
PAGE_SIZE_MEDIUM = 10
PAGE_SIZE_BIG = 20


PAPER_STATUS_NOT_GENERATED = 0
PAPER_STATUS_GENERATING = 1
PAPER_STATUS_GENERATED = 2


BASE_YEAR = 2009

EDU_YUN_FORMAL = 1


STUDENT_EXERCISE_WAIT_FOR_DO = 0
STUDENT_EXERCISE_WAIT_FOR_CORRECTED = 1
STUDENT_EXERCISE_DONE = 2


PUBLISH_INFO_WAIT_FOR_DO = 0
PUBLISH_INFO_WAIT_FOR_CORRECTED = 1
PUBLISH_INFO_DONE = 2
PUBLISH_INFO_NO_PUBLISH = 3

# 布置的试卷的模式
COMMIT_MODE_ONLINE = 0
COMMIT_MODE_OFFLINE = 1
COMMIT_MODE_UNCORRECT = 2

# 校本题库权限
SCHOOL_BANK_RIGHT_DEL = -2  # 删除
SCHOOL_BANK_RIGHT_UNPASS = -1  # 未通过审核的
SCHOOL_BANK_RIGHT_NONE = 0  # 没有权限的
SCHOOL_BANK_RIGHT_PASS = 1  # 通过审核
SCHOOL_BANK_RIGHT_UPLOAD = 2  # 具有上传权限
SCHOOL_BANK_RIGHT_ADMIN = 3  # 学科校本题库管理员

# 校本试卷状态
SCHOOL_PAPER_STATUS_DEL = -2  # 已经删除
SCHOOL_PAPER_STATUS_UNPASS = -1  # 审核不通过
SCHOOL_PAPER_STATUS_NEW = 0  # 待审核
SCHOOL_PAPER_STATUS_DOING = 1  # 审核通过正在录排
SCHOOL_PAPER_STATUS_DONE = 2  # 完成录排


# 校本试题状态
SCHOOL_ITEM_STATUS_DEL = -2  # 已经删除
SCHOOL_ITEM_STATUS_UNPASS = -1  # 审核不通过
SCHOOL_ITEM_STATUS_NEW = 0  # 待审核
SCHOOL_ITEM_STATUS_DOING = 1  # 审核通过正在录排
SCHOOL_ITEM_STATUS_DONE = 2  # 完成录排


# 账号自管理状态
ACCOUNT_RIGHT_NONE = 0
ACCOUNT_RIGHT_STUDENT = 1
ACCOUNT_RIGHT_TEACHER = 2
ACCOUNT_RIGHT_ADMIN = 3
