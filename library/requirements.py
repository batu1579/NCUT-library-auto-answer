#!/usr/bin/env python
# coding=utf-8
'''
Author: BATU1579
Date: 2021-08-12 05:08:15
LastEditors: BATU1579
LastEditTime: 2021-09-04 18:43:19
Description: 初次运行时安装依赖文件
'''
from pip._internal import main
from json import load, dump


with open(".\\library\\run_time.json", "r") as fp:
    data = load(fp)

if data["is_first_time"]:
    # -q参数让pip减少输出
    main(['install', '-r', 'requirements.txt'])
    data["is_first_time"] = False

with open(".\\library\\run_time.json", "w+") as fp:
    dump(data, fp)
