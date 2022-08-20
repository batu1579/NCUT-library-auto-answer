#!/usr/bin/env python
# coding=utf-8
'''
Author: BATU1579
CreateDate: 2021-08-12 04:31:20
LastEditor: BATU1579
LastTime: 2022-08-20 20:37:04
FilePath: \\library\\settings.py
Description: scripts settings
'''

# TODO 改换成ini格式的文档，用来支持读写

# 开发者模式（输出更详细的日志）
dev_mode = False

# 驱动文件地址（如果没有为空即可，会自动下载匹配的驱动）
driver_path = ""

# 本机使用的浏览器（要与所使用的驱动文件对应）
#  - edge
#  - chrome
#  - firefox
browser = "edge"

# Github个人令牌（防止github访问限制导致的下载驱动失败）
GitHub_token = ""

# 每次获取元素时等待的时间（秒）
wait_time = 0.1

# 运行时显示浏览器窗口
show_window = True

# 验证码图片地址
veri_code_path = ".\\src\\img\\veri_code.png"

# 验证码图像阈值
threshold_value = 130

# 手动输入验证码
use_input_veri = True

# 使用百度api识别验证码
use_baidu_api = False

# api认证信息存放位置
api_token_path = ".\\api_token.json"

# 调用api时重试的次数
retry_num = 3

# 使用的皮肤（如果已经登录选择过皮肤则必须与当前的皮肤一致）
#  - school: 校园版
#  - student: 书生版
#  - warrior: 战士版
theme = "student"
