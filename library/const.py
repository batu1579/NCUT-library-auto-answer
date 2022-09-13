#!/usr/bin/env python
# coding=utf-8
'''
Author: BATU1579
CreateDate: 2021-08-10 16:49:21
LastEditor: BATU1579
LastTime: 2022-09-13 09:17:48
FilePath: \\library\\const.py
Description: 存储常量
'''
from loguru import logger
from sys import stderr

from library.use_data import get_json_data
from library import settings

# 日志文件
LOG = logger
LOG.remove()
LOG.add(".\\logs\\logs-{time}.log",
        retention=10,
        encoding="utf-8",
        level="DEBUG")

# 读取常量

DEV_MODE = settings.dev_mode

DRIVER_PATH = settings.driver_path
BROWSER = settings.browser
GH_TOKEN = settings.GitHub_token
WAIT_TIME = settings.wait_time
SHOW_WINDOW = settings.show_window

VERI_CODE_PATH = settings.veri_code_path
THRESHOLD_VALUE = settings.threshold_value

USE_INPUT_VERI = settings.use_input_veri

USE_BAIDU_API = settings.use_baidu_api
API_TOKEN_PATH = settings.api_token_path
RETRY_NUM = settings.retry_num

THEME_NAME = settings.theme

# 读取皮肤文件
THEME = get_json_data(".\\src\\themes\\%s.json" % settings.theme)

# 控制台日志
LOG.add(stderr, level="DEBUG" if DEV_MODE else "INFO")
