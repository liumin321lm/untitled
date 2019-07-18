from selenium import webdriver

import logging.config
import os
#CON_LOG=r'D:\py_project\Auto_Test_project\Website\log\log.conf'

# CON_LOG='../log/log.conf'
#
# logging.config.fileConfig(CON_LOG)
# logging=logging.getLogger()
#current_path = os.path.abspath('..')
current_path = os.path.dirname(os.path.dirname(__file__))
#print(current_path)
CON_LOG=os.path.abspath(os.path.join(current_path,'./Website/log/log.conf'))
#CON_LOG=os.path.abspath(os.path.join(os.getcwd(), "log.conf"))
#print(CON_LOG,'111111')
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()



def browser():


    driver=webdriver.Chrome()
    #a=driver.switch_to.frame('400000100frame')
    return driver

if __name__ == '__main__':
    browser()
