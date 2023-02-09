#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2021/8/3 11:34
# @Author:lucky
# @Email:
# @File:handle_config.py

from configparser import ConfigParser
from common.handle_path import conf_dir
import os

# class HandleConfig:
#     """
#     读取配置文件类
#     """
#     def read_config(self,filename,section,value):
#         # 第一步：创建一个配置文件解析器对象
#         cp = ConfigParser()
#         # 第二步 读取配置文件中的内容到配置文件解析器中
#         cp.read(filename,encoding='utf-8')
#         # 第三步 读取配置内容，get 读取字符串
#         # getint,读数值，getboolean，布尔值，getfloat 浮点类型
#         res = cp.get(section,value)
#         return res
#
#     def write_config(self,filename,section,name,value):
#         # 第一步：创建一个配置文件解析器对象
#         cp = ConfigParser()
#         # 第二步 读取配置文件中的内容到配置文件解析器中
#         cp.read(filename, encoding='utf-8')
#         # 第三步 设置内容
#         cp.set(section,name,value)
#         #第四步 写入到ini文件中
#         cp.write(fp=open(filename,'w',encoding='utf-8'))

# 继承ConfigParser类

class HandleConfig(ConfigParser):
    """
    创建对象时,直接加载配置文件中的内容
    重写了configParse的__init__方法
    在init方法中添加了调用read读取配置文件的操作

    """
    def __init__(self,config_file):
        # 重写init方法
        super().__init__()
        self.read(config_file,encoding='utf-8')

# 创建实例

conf = HandleConfig(os.path.join(conf_dir,"config.ini"))

if __name__ == '__main__':
    name = conf.get("test_data","username")
    print(name)