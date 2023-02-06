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


# report_dir=os.path.join(REPORTS_DIR,filename)

#执行前，删除reports中的文件
# log.info("执行测试前，清空reports文件夹内容")
os.system('cd reports && del * /q && cd ..')
#删除日志内容
# log.info("清空日志文件")
# os.system('cd ./logs && del * /q')

pytest.main(['testcases/huarun999/test_huarun999_middle.py','-s','-v','--alluredir=reports'])