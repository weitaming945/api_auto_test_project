#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2022/9/14 12:08
# @Author:lucky
# @Email:
# @File:conftest.py
import json
import unittest

import pytest

from common.handle_config import conf
import requests
import json
from common.handle_excel import HandleExcel
from common.handle_path import data_dir
import os
from common.handle_re import get_attr,replace_data
from common.handle_dynamic_data import Data
import time
from common.handle_sql import db



@pytest.fixture(scope='class')
def test_huarun_login():
    #登录接口，请求参数
    login_data={
          "type": 0,
          "accountName": "admin",
          "password": "5L9lZYiGBcRUEt9aQRdXZw=="
        }
    #登录接口，请求地址
    login_url=conf.get("url","url_admin")+"/sanjiu-admin-server/sys/login"
    #登录接口，请求方式
    login_method="POST"
    #登录接口，请求头
    login_headers={"Content-Type": "application/json","charset":"utf-8"}
    #发起请求
    res=requests.request(method=login_method,json=login_data,headers=login_headers,url=login_url)

    #响应内容转化json字符串
    res=res.json()

    #取token值，保存为属性名：authorization
    json_exp='$.data.token'
    attr_name='authorization'
    attr_value=get_attr(res,json_exp,attr_name)
    print(attr_value)
    print('已添加属性名{},属性值{},到Data类属性'.format(attr_name, attr_value))


@pytest.fixture(scope='class')
def test_data_clear():
    """
    此方法为连接数据库删除新增的用户数据
    页面上无入口直接删除用户
    """
    #测试执行前先删除用户-避免在测试过程中添加失败
    sql='delete FROM cr_sanjiu.user_info where mobile = "00000000000"'
    db.delete_data(sql)
    yield
    #测试执行完成后，删除用户
    sql = 'delete FROM cr_sanjiu.user_info where mobile = "00000000000"'
    db.delete_data(sql)



#退出登录
def test_huarun_logout():
    #生成13位时间戳
    timestamp=int(time.time()*1000)
    # print(timestamp) #1663143037993

    logout_data={""}
    logout_url=conf.get("url","url_admin")+"/sys/logout"
    logout_method="POST"
    logout_headers={"Content-Type": "application/json","charset":"utf-8"}
    res = requests.request(method=logout_method,json="",headers=logout_headers, url=logout_url)
    res = res.json()
    print(res)


if __name__ == '__main__':

    test_huarun_login()
    test_huarun_logout()





