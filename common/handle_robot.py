#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2023/2/9 10:38 
# @Author : liuling 
# @File : handle_robot.py 
# @desc:

import datetime
import requests
from common.handle_config import conf

headers={"Content-Type":"application/json"}

#机器人的webhook地址
webhook_address=conf.get("webhook","webhook_address")

class Robot:

    def message(self,projectname,total,passed,failed,skipped,address):
        time=datetime.datetime.now()
        data={
            "msgtype": "markdown",
            "markdown": {
                "content":
                    '''<font color=\"warning\">提醒！自动化测试反馈\n请相关同事注意，及时跟进！</font>\n
                    > 用例执行完毕时间:<font color=\"info\">{}</font>\n
                    > 项目名称:<font color=\"comment\">{}</font>\n
                    > 用例总数:<font color=\"comment\">{}</font>\n
                    > 通过用例数:<font color=\"info\">{}</font>\n
                    > 失败用例数:<font color=\"warning\">{}</font>\n
                    > 跳过用例数:<font color=\"warning\">{}</font>
                    > 报告链接：[allure报告,请点击后进入查看]({})
                '''.format(time, projectname, total, passed, failed, skipped, address)
                     }
            }

        return data

    def sendMessage(self,projectname,total,passed,failed,skipped,address):
        data=self.message(projectname,total,passed,failed,skipped,address)
        requests.post(url=webhook_address,headers=headers,json=data)
        print("发消息了")

robot=Robot()
