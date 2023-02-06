# -*- coding:utf-8 -*-
# @Time:2021/8/3 16:01
# @Author:lucky
# @Email:
# @File:handle_path.py

import os
"""
此模块用来处理项目中的绝对路径
"""

# # 获取当前文件的文件名
# # fp = __file__
# # 获取当前的绝对路径
# fp = os.path.abspath(__file__)
# print(fp)
# # 获取当前文件的上一级目录
# path1 = os.path.dirname(fp)
# print(path1)

# 获取项目根目录的绝对路径  D:\TOOLS\python_demo
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 路径拼接 D:\TOOLS\python_demo\datas
# data_dir = os.path.join(base_dir, "datas")


# 用例数据所在目录
data_dir = os.path.join(base_dir, "datas")

# 配置文件所在目录
conf_dir = os.path.join(base_dir, "conf")

# 日志文件所在目录
log_dir = os.path.join(base_dir, "logs")

# 测试报告所在目录
reports_dir = os.path.join(base_dir, "reports")

# 测试数据所在目录
testcases_dir = os.path.join(base_dir, "testcases")