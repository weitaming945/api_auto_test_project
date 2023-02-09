#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2021/8/3 9:39
# @Author:lucky
# @Email:
# @File:handle_log.py
import logging
import sysconfig

from common.handle_config import conf
from common.handle_path import log_dir
import os
import time


def create_log(name="my_log", filename="log.log", level="DEBUG", sh_level="DEBUG", fh_level="DEBUG"):
    """

    :param name: 日志收集器名字
    :param filename: 日志文件名
    :param level: 收集日志等级
    :param sh_level: 输出到控制台日志等级
    :param fh_level: 输出到文件日志等级
    :return:
    """
    # 第一步 创建日志收集器
    log = logging.getLogger(name)

    # 第二步 设置收集器收集日志的等级
    log.setLevel(level)

    # 第三步 设置日志输出渠道
    # 3.1 输出到文件的配置
    fh = logging.FileHandler(filename, encoding="utf-8")
    fh.setLevel(fh_level)
    log.addHandler(fh)

    # 3.2输出到控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)

    # 第四步 设置日志输出的格式
    # 4 设置日志输出的等级
    # 将格式保存到formats变量中
    formats = '%(asctime)s-[%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
    log_format = logging.Formatter(formats)
    # 为输出渠道设置输出格式
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)

    # 返回一个日志收集器
    return log

# 为了避免程序中创建多个日志收集器而导致日志重复记录
# 创建日志收集器,测试方法调用时,from handle_log import my_log,可以直接使用my_log.error("内容")
# my_log = create_log()

# 调用配置文件中的内容,conf是handle_config.py中的定义的变量,导入调用
# 若要更改,直接更改配置文件中的值

# filename,传入路径加文件名

log = create_log(
                    name=conf.get("logging","name"),
                    level=conf.get("logging","level"),
                    filename=os.path.join(log_dir,conf.get("logging","filename"))+".log",
                    sh_level=conf.get("logging","sh_level"),
                    fh_level=conf.get("logging","fh_level")
                    )
# print(conf.get("logging","name")+"_"+ time.strftime("%Y%m%d%H%M%S"))
# filename=os.path.join(log_dir,conf.get("logging","filename"))+"_"+ time.strftime("%Y%m%d%H%M%S")+".log",


