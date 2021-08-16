#!/usr/bin/env python
# coding=utf-8
'''
Author: BATU1579
Date: 2021-08-11 15:20:04
LastEditors: BATU1579
LastEditTime: 2021-08-16 22:33:54
Description: file content
'''
import logging
import library.const as g
from time import sleep


def set_github_token():
    if g.GH_TOKEN != "":
        # 设置github访问令牌
        import os
        os.environ['GH_TOKEN'] = g.GH_TOKEN
        g.LOG.debug("设置环境变量GH_TOKEN为: %s" % g.GH_TOKEN)
    else:
        g.LOG.warning("未设置github个人令牌，可能会因为访问限制下载驱动失败")


# 加载不同浏览器的驱动
if g.BROWSER == "edge":
    # edge驱动设置
    from msedge.selenium_tools import Edge as Driver
    from library.webdriver_manager.microsoft import EdgeChromiumDriverManager as Manager
    from msedge.selenium_tools import EdgeOptions
    options = EdgeOptions()
    options.use_chromium = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 不显示日志

elif g.BROWSER == "chrome":
    # chrome驱动设置
    from selenium.webdriver import Chrome as Driver
    from library.webdriver_manager.chrome import ChromeDriverManager as Manager
    from selenium.webdriver import ChromeOptions
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 不显示日志

elif g.BROWSER == "firefox":
    # firefox驱动设置
    from selenium.webdriver import Firefox as Driver
    from library.webdriver_manager.firefox import GeckoDriverManager as Manager
    from selenium.webdriver import FirefoxOptions
    options = FirefoxOptions()
    set_github_token()

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


def common_options():
    # 各个浏览器的通用设置
    options.add_argument("–-incognito")  # 无痕模式
    if not g.SHOW_WINDOW:
        options.add_argument("--handless")


def get_broswer():
    driver_path = g.DRIVER_PATH

    if driver_path == "":
        # 下载匹配的驱动
        driver_path = Manager(
            path=".\\src",
            print_first_line=False,
            cache_valid_range=10,
        ).install()

    # 加载通用配置
    common_options()

    # 创建浏览器
    broswer = WaitDriver(executable_path=driver_path, options=options)
    return broswer
