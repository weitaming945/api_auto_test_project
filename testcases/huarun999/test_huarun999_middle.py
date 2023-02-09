#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2022/8/18 12:23
# @Author:lucky
# @Email:
# @File:test_huarun999.py

from common.handle_excel import HandleExcel
import os
from common.handle_log import log
from common.handle_path import data_dir
import pytest
from common.handle_config import conf
import requests
from common.handle_re import replace_data, get_attr
from common.handle_dynamic_data import Data
import allure
import json
from common.handle_sql import db

# 读excel数据
test_data = HandleExcel(os.path.join(data_dir, 'huarun999/huarun999_middle.xlsx'))
# 生成测试数据
data = test_data.read_excel_api_cases()

class TestPsmApi:


    @allure.epic("华润999中台")
    @pytest.mark.parametrize('cases', data)
    def test_psm_api(self, cases,false=''):

        # 打印当前执行的用例信息
        # print('当前执行的用例是：【{}】-【{}】-【{}】-【{}】'.format(cases['module'],cases['sub_module'],cases['case_id'],cases['title']))
        log.info('当前执行的用例是：【{}】-【{}】-【{}】-【{}】-【{}】'.format(cases['feature'], cases['module'], cases['sub_module'],
                                                            cases['case_id'], cases['title']))
        # 拼接url
        url = conf.get('url', 'url_admin') + cases['path']
        # print('当前的url地址是:',url)

        # #动态获取模块名称。
        allure.dynamic.feature(cases['feature'])
        # #动态获取子模块（二级模块），
        allure.dynamic.story(cases['module'])
        # 动态获取用例标题
        allure.dynamic.title(cases['title'])


        # 判断替换变量是否为空,不为空,则表示在执行前有变量要替换
        if cases['replace_var'] != '':
            header = eval(replace_data(cases['headers']))
            data = eval(replace_data(cases['data']))
        else:
            header = eval(cases['headers'])
            if cases['data'] == None:
                data = None
            else:
                data = eval(replace_data(cases['data']))

        log.info("当前执行用例的url地址是:{}".format(url))
        log.info("当前执行用例的请求头是:{}".format(header))
        log.info("当前执行用例的请求数据是:{}".format(data))


        if cases['method'] == 'get':
            # 获取到的请求方法,如果是小写,转换成大写
            method = cases['method'].upper()
            response = requests.request(method=method, url=url, params=data, headers=header)
        elif cases['method'] == 'post':
            method = cases['method'].upper()
            # response = requests.request(method=method, url=url, json=data, headers=header)
            response = requests.request(method=method, url=url, json=data, headers=header)
        elif cases['method']=='put':
            method=cases['method'].upper()
            response=requests.request(method=method,url=url,json=data,headers=header)
        elif cases['method']=='delete':
            method=cases['method'].upper()
            response=requests.request(method=method,url=url,params=data,headers=header)

        # 返回响应内容，字典格式
        res = response.json()
        # print(res)
        # log.info("当前执行用例的响应结果是:{}".format(res))
        # print(res.get)

        # 判断断言字段是否有值，若有值，则根据此字段判断，若无值，则判断响应状态码
        try:
            if cases['expect_res_assert_field'] != None:
                assert cases['expect_res_assert_code'] == res.get(cases['expect_res_assert_field'])
            else:
                assert response.status_code == cases['expect_status_code']
        except Exception as e:
            log.error('断言失败，用例执行不通过')
            log.info("当前执行用例的响应结果是:{}".format(res))
            log.error(e)
            assert False
        else:
            log.info('断言成功,用例执行通过')
            log.info("当前执行用例的响应结果是:{}".format(res))


        # # 判断get_value是否有值,有值则将值写入到类属性中
        # if cases['get_value'] != None:
        #     response_data = res
        #     json_exp = cases['json_exp']
        #     attr_name = cases['get_value']
        #     attr_value = get_attr(res, json_exp, attr_name)
        #     # print('已添加属性名{},属性值{},到Data类属性'.format(attr_name,attr_value))
        #     log.info('已添加属性名{},属性值{},到Data类属性'.format(attr_name, attr_value))
        # else:
        #     pass

        if cases['get_value_jsonpath']!=None:
            response_data=res
            #cases['get_value_jsonpath'],取到的值为字典
            # print(cases['get_value_jsonpath'],type(eval(cases['get_value_jsonpath'])))
            #用一个字典保存
            dic=eval(cases['get_value_jsonpath'])
            #循环取要取的属性的值，并添加到类属性中
            for i in dic:
                #dic.get(i)，取i对应的value值
                json_exp=dic.get(i)
                attr_name=i
                attr_value=get_attr(res,json_exp,attr_name)
                # print('已添加属性名{},属性值{},到Data类属性'.format(attr_name, attr_value))
                log.info('已添加属性名{},属性值{},到Data类属性'.format(attr_name, attr_value))
        else:
            pass
