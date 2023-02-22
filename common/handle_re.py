#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2021/8/13 12:01
# @Author:lucky
# @Email:
# @File:handle_re.py
import re
from common.handle_config import conf
from jsonpath import jsonpath
import json
from common.handle_dynamic_data import Data
from common.handle_log import log

def replace_data(data):
    """
    替换数据的方法
    :param data: 要进行替换的用例数据（字符串）
    :return:
    """
    while re.search('#(.+?)#',data): # while为true时，循环执行
        res = re.search('#(.+?)#',data) # 返回类
        item = res.group() #  获取第一个#中的内容 比如 #id#
        attr = res.group(1) # 获取到的#内的内容，比如 id
        try:
            value = getattr(Data,attr) # 获取到类中定义的属性值
        except AttributeError:
            value = conf.get('test_data',attr) # 从配置文件中找
        data = data.replace(item,str(value)) # 将字符串中的与类中的属性值做替换
    return data



def get_attr(response_data,json_exp,attr_name):
    """
    jsonpath替换,提取接口返回数据
    :param response_data: 接口响应内容
    :param json_exp: jsonpath表达式
    :return: 返回取到的值
    """
    try:
        attr_value=jsonpath(response_data,json_exp)[0]
    except Exception as e:
        log.info("获取属性值失败")
        raise e
    else:
        setattr(Data,attr_name,attr_value)
    return attr_value



if __name__ == '__main__':
    pass