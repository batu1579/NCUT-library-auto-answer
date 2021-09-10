#!/usr/bin/env python
# coding=utf-8
'''
Author: BATU1579
Date: 2021-08-10 16:49:21
LastEditors: BATU1579
LastEditTime: 2021-09-04 18:46:23
Description: 存储常量
'''
from loguru import logger
from library.use_data import get_json_data
from sys import stderr
import library.settings as profile


# 日志文件
LOG = logger
LOG.remove()
LOG.add(
    ".\\logs\\logs-{time}.log",
    retention=10,
    encoding="utf-8",
    level="DEBUG"
)

# 读取常量

CONST = profile.script_settings

DEV_MODE        = CONST["dev_mode"]

DRIVER_PATH     = CONST["driver_path"]
BROWSER         = CONST["browser"]
GH_TOKEN        = CONST["GitHub_token"]
WAIT_TIME       = CONST["wait_time"]
SHOW_WINDOW     = CONST["show_window"]

VERI_CODE_PATH  = CONST["veri_code_path"]
THRESHOLD_VALUE = CONST["threshold_value"]

USE_INPUT_VERI  = CONST["use_input_veri"]

USE_BAIDU_API   = CONST["use_baidu_api"]
API_TOKEN_PATH  = CONST["api_token_path"]
RETRY_NUM       = CONST["retry_num"]

# 读取皮肤文件
THEME = get_json_data(".\\src\\themes\\%s.json" % CONST["theme"])

# 控制台日志
LOG.add(
    stderr,
    level="DEBUG" if DEV_MODE else "INFO"
)