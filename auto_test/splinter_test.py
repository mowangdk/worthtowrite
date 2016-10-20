#!/usr/bin/env python
# fileencoding=utf-8

import sys

import re
import traceback

from splinter.browser import Browser


browser = Browser('chrome')


def work():
    try:
        url = "http://www.kuailexue.com"
        browser.visit(url)

        with browser.get_iframe(0) as iframe:

            iframe.find_by_id('email').fill('banzhuren')
            iframe.find_by_id('password').fill('qwer1234')
    #       browser.fill('password', 'qwer1234') # 直接fill只对name有效
            button = iframe.find_by_id('login').first
            button.click()
        # 出题组卷
        browser.click_link_by_partial_href('choose_template')
        # 章节练习
        browser.click_link_by_partial_href('new/set_template_parameters?tname=danyuanceshi')    # success# success
        # first page
        home_windows = browser.windows.current

        chapter_chuti()

        # browser.click_link_by_text('第二章  基本初等函数（I）')
        # # test find password
        # output("测试找回密码链接")
        # browser.visit(__testUrl)
        # backPasswordLink = browser.find_link_by_text('取回密码')
        # if 1 == len(backPasswordLink):
        #     backPasswordLink.first.click()
        #     ru = re.findall(re.compile(".*(reg/gp.htm).*", re.IGNORECASE), browser.url)
        #     if ru is not None:
        #         checkresult('找回密码')
        #     else:
        #         output('测试找回密码链接失败')
    except Exception, x:
        print traceback.print_exc()
        print x


def chapter_chuti():

    browser.windows.current = browser.windows[1]
    unit_textbook = browser.find_by_id('unit_textbook')
    unit_textbook_tree = browser.find_by_id('unit_textbook_tree')[0]
    sec_level = unit_textbook_tree.find_by_id('sec_level')
    for unit_text in unit_textbook.find_by_tag('label'):
        unit_text.click()
        for href in sec_level.find_by_tag('a'):
            href.click()
            # third_level = unit_textbook_tree.find_by_id('thi_level')
            # map(lambda x: x.check(), [checkbox for checkbox in third_level.find_by_tag('input')])
            unit_textbook_tree.find_by_id('check_all').first.check()
    browser.find_by_id('template_next').first.click()


if __name__ == '__main__':
    work()
