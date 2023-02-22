#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2023/2/16 12:15 
# @Author : liuling 
# @File : handle_data.py 
# @desc:

import math
import random
import hashlib
import time
from common.handle_dynamic_data import Data
import time

"""
华润项目，登录时，请求头中，新增3个字段值，定义两个方法，getNoncestr，getSignature,动态取值

"""

def get_noncestr():
    #从大小写字母+数字中，随机取32个字符，拼成字符串
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    noceStrList = []
    for i in range(0, 32):
        index = math.floor(random.random() * len(chars))
        # print(index)
        noceStrList.append(chars[index])
        # noceStrList.append(chars.index())

    noncestr = "".join(noceStrList)
    # 设置为Data的类属性
    setattr(Data, "noncestr", noncestr)

    return noncestr


def get_timestamp():
    # 获取时间戳，13位
    timestamp = str(int(round(time.time() * 1000)))
    # 设置为Data的类属性
    setattr(Data, "timestamp", timestamp)

    return timestamp


def get_signature(noncestr=0,timestamp=0,SIGN_KEY=0):
    # md5加密，加密规则需要开发提供
    # str_md5="x-noncestr="+noncestr+"&x-timestamp="+str(timestamp)+"&key="+SIGN_KEY
    str_md5="x-noncestr={}&x-timestamp={}&key={}".format(noncestr,timestamp,SIGN_KEY)
    md=hashlib.md5(str_md5.encode())
    signature=md.hexdigest()

    # 设置为Data的类属性
    setattr(Data, "signature", signature)

    return signature






if __name__ == '__main__':

    noncestr=get_noncestr()
    print(noncestr,type(noncestr))
    timestamp=get_timestamp()
    print(timestamp,type(timestamp))
    SIGN_KEY = "cf37fHp7zY2wRB7fa5KcDb31cdUFc8a5fc"
    signature=get_signature(noncestr,timestamp,SIGN_KEY)
    print(signature,type(signature))
    print(Data().noncestr)
    print(Data().timestamp)
    print(Data().signature)