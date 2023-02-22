#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2022/8/18 14:14
# @Author:lucky
# @Email:
# @File:handle_dynamic_data.py
import random
import time
# from common.handle_data import getNoncestr,getSignature


class Data:
    """
    此类用于存放测试过程中的动态数据
    使用方式,将上一个接口返回的数据,提取后,保存为此类的类属性
    下一个接口要进行数据替换时,从此类中匹配
    """
    # 华润项目变量
    username = 'admin'
    password='4nuL1fAvAPech6Kj/s+x4g=='
    # 随机生成9位数字
    number = random.randint(10000000000, 99999999999)
    # 员工姓名
    name="测试"+str(number)
    # 地区 大区
    area="上海区域"
    areaCode=198020
    cityCode=197300
    deptId="0bd1176ed8f7fb0ec470db8d71f1139e"
    region="华东大区"
    provinceCode=190000
    roleId="e852b143b8202a1094ec2738bb12f56e"


data=Data()

if __name__ == '__main__':

    noncestr="0UMBqP3ID5NK8qes2v6W46o3yxwd2vXT"
    timestamp=1676523713055
    print(Data().number)