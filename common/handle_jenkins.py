#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2023/2/9 9:43 
# @Author : liuling 
# @File : handle_jenkins.py 
# @desc:

import jenkins
from common.handle_config import conf
from common.handle_log import log

class JenkinsConnect:
    def __init__(self):
        self.jenkins_url=conf.get("jenkins","jenkins_url")
        self.jenkins_username=conf.get("jenkins","jenkins_username")
        self.jenkins_pwd=conf.get("jenkins","jenkins_pwd")


    #连接jenkins服务器，需要jenkins的登录地址，用户名，密码
    def jenkins_connect(self):
        try:
            server=jenkins.Jenkins(url=self.jenkins_url,username=self.jenkins_username,password=self.jenkins_pwd)
            print(self.jenkins_url)
            return server
        except Exception as e:
            log.error("连接jenkins服务器失败，失败原因{}".format(e))
            return None

    #获取上一次构建任务的相关信息
    def get_project_run_info(self,projectname,key):
        service=self.jenkins_connect()
        if service:
            value=service.get_job_info(projectname)[key]
            return value
        else:
            return None

    #拼接allure地址，获取上一次构建成功后的allure地址
    def get_allure_address(self,projectname,key):
        num = self.get_project_run_info(projectname,key)
        if num:
            #报告地址参考：http://172.29.95.187:9999/job/auto_test_sanjiu_project/7/allure/
            allure_address=self.jenkins_url+"/job/projectname/{}/allure/".format(num-1)
            return allure_address
        else:
            return None

jenk=JenkinsConnect()

if __name__ == '__main__':
    projectname=conf.get("jenkins","project_name")
    value=jenk.get_allure_address(projectname=projectname,key="nextBuildNumber")
    print(value)
    # jenk.jenkins_connect()

