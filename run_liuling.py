#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time:2021/6/21 16:11
# @Author:lucky
# @Email:
# @File:run.py

from common.handle_path import testcases_dir,reports_dir
import time
import os
import pytest
from common.handle_log import log
from pytest_jsonreport.plugin import JSONReport
from common.handle_robot import robot
from common.handle_jenkins import jenk
from common.handle_config import conf

# report_dir=os.path.join(REPORTS_DIR,filename)

#执行前，删除reports中的文件
# log.info("执行测试前，清空reports文件夹内容")
os.system('cd reports && del * /q && cd ..')
#删除日志内容
# log.info("清空日志文件")
# os.system('cd ./logs && del * /q')

#需要生成结果文件，不然jenkins识别不出来
plugin=JSONReport()
# 报告存放的位置
pytest.main(['testcases/huarun999/test_huarun999_middle.py','-s','-v','--alluredir=reports'],plugins=[plugin])

summary=plugin.report.get("summary")
#得到通过，失败，跳过和总执行的用例数
passed=summary.get("passed",0)
failed=summary.get("failed",0)
skipped=summary.get("skipped",0)
total=summary.get("total",0)


#获取地址
#获取项目名称
projectname=conf.get("jenkins","project_name")
address=jenk.get_allure_address(projectname=projectname,key="nextBuildNumber")
print(address)

#发送企业微信消息
robot.sendMessage(projectname=projectname,total=total,passed=passed,skipped=skipped,failed=failed,address=address)