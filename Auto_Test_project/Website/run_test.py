import unittest
from function import *
import time
from HTMLTestRunner import HTMLTestRunner

# import sys
# path=r'D:\py_project'
# sys.path.append(path)

import logging
import logging.config
# CON_LOG='./log/log.conf'
# logging.config.fileConfig(CON_LOG)
# logging=logging.getLogger()

report_dir='./test_report'
test_dir='./test_case'

logging.info("start run test case")
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")

now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+'/'+now+'result.html'
logging.info("start write report..")
with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title="Test Report",description="localhost test")
    runner.run(discover)
f.close()


logging.info("find latest report")
latest_report=latest_report(report_dir)
logging.info("send email report..")
send_mail(latest_report)
logging.info("Test end!")



