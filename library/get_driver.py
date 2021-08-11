#!/usr/bin/env python
# coding=utf-8
'''
Author: BATU1579
Date: 2021-08-11 15:20:04
LastEditors: BATU1579
LastEditTime: 2021-08-11 22:04:38
Description: file content
'''
import logging
import library.const as g
from time import sleep


# 加载不同浏览器的驱动
if g.BROWSER == "edge":
    from msedge.selenium_tools import Edge as Driver
    from webdriver_manager.microsoft import EdgeChromiumDriverManager as Manager
    from msedge.selenium_tools import EdgeOptions
    options = EdgeOptions()
    # edge驱动设置
    options.use_chromium = True
    options.add_argument("–-incognito")  # 无痕模式
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 不显示日志
    if not g.SHOW_WINDOW:
        options.add_argument("handless")
    options.add_argument("--disk-cache-dir=%s" % g.CACHE_PATH)
    options.add_argument("–-disk-cache-size=%d" % g.CACHE_SIZE)

elif g.BROWSER == "chrome":
    from selenium.webdriver import Chrome as Driver
    from webdriver_manager.chrome import ChromeDriverManager as Manager
    from selenium.webdriver import ChromeOptions
    options = ChromeOptions()
    # chrome驱动设置
    options.add_argument("–-incognito")  # 无痕模式
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 不显示日志
    if not g.SHOW_WINDOW:
        options.add_argument("handless")
    options.add_argument("--disk-cache-dir=%s" % g.CACHE_PATH)
    options.add_argument("–-disk-cache-size=%d" % g.CACHE_SIZE)

# TODO 对firefox浏览器的支持
else:
    g.LOG.error("暂不支持 %s 浏览器" % g.BROWSER)
    exit()


class WaitDriver(Driver):
    def find_element_by_id(self, id_):
        sleep(g.WAIT_TIME)
        return super().find_element_by_id(id_)
    def find_element_by_css_selector(self, css_selector):
        sleep(g.WAIT_TIME)
        return super().find_element_by_css_selector(css_selector)


def get_broswer():
    driver_path = g.DRIVER_PATH
    if driver_path == "":
        # 下载匹配的驱动
        driver_path = Manager(
            path=".\\src",
            print_first_line=False,
            cache_valid_range=10,
        ).install()
    broswer = WaitDriver(driver_path, options=options)
    return broswer
