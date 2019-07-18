import smtplib
import unittest
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from HTMLTestRunner import *
import os
import time

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver='smtp.qq.com'

    user='1301073951@qq.com'
    password='dkghsefbvnyrjafc'

    sender='1301073951@qq.com'
    receives=['5431523@qq.com','340497963@qq.com']

    subject='Web Selenium 自动化测试报告'

    #content='<html><h1 style="color:red"> Selenium1111111111</h1></html>'

    # send_file=open(r'E:\xunlei\logo.txt','rb').read()
    # att=MIMEText(send_file,'base64','utf-8')
    # att['Content-Type']='application/octet-stream'
    # att['Content-Disposition']='attachment;filename="logo.txt"'
    msgRoot=MIMEMultipart()
    msgRoot.attach(MIMEText(mail_content,'html','utf-8'))
    msgRoot['Subject']=subject
    msgRoot['From']=sender
    msgRoot['To']=','.join(receives)
    #msgRoot.attach(att)

    # msg=MIMEText(content,'html','utf-8')
    # msg['Subject']=Header(subject,'utf-8')
    # msg['From']=sender
    # msg['To']=','.join(receives)

    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user,password)
    print("Start send Email")
    smtp.sendmail(sender,receives,msgRoot.as_string())
    smtp.quit()
    print("Send Email end!")

def latest_report(report_dir):
    lists=os.listdir(report_dir)
    print(lists)
    lists.sort(key=lambda  fn: os.path.getatime(report_dir+'\\'+fn))
    print("the latest report is " + lists[-1])
    file=os.path.join(report_dir, lists[-1])
    print(file)
    return file

if __name__ == '__main__':

    report_dir='./test_report'
    test_dir='./test_case'

    print("start run test case")
    discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_login.py")

    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+'/'+now+'result.html'
    print("start write report..")
    with open(report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title="Test Report",description="localhost login test")
        runner.run(discover)
        f.close()

    print("find latest report")
    latest_report=latest_report(report_dir)
    print("send email report..")
    #send_mail(latest_report)
    send_mail(latest_report)
    print("Test end!")


