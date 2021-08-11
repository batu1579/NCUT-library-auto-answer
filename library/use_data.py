#!/usr/bin/env python
# coding=utf-8
'''
Author: BATU1579
Date: 2021-08-10 17:11:55
LastEditors: BATU1579
LastEditTime: 2021-08-11 20:52:07
Description: file content
'''
from json5 import load, dump
import library.const as g


def get_file_data(file_path: str) -> dict:
    g.LOG.debug("正在从文件 {file_path} 中读取数据")
    with open(file_path, "rb") as fp:
        return fp.read()


def get_json_data(file_path: str) -> dict:
    g.LOG.debug("正在从文件 {file_path} 中读取json数据")
    with open(file_path, "rb") as fp:
        return load(fp)


def save_json_data(file_path: str, data: dict):
    g.LOG.debug("正在向文件 {file_path} 中存储json数据")
    with open(file_path, "w+") as fp:
        dump(data, fp, indent=2)
