# coding=utf-8
from telnetlib import EC

from appium import webdriver
from time import sleep
import time
import unittest
import warnings

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
class Test_case(unittest.TestCase):

    def setUp(self):
        proposal = {}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '9.0'
        proposal['deviceName'] = '520083b6b820250b'
        proposal['appPackage'] = 'com.tal.kaoyan'
        proposal['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
        proposal['automationName'] = 'uiautomator2'
        proposal['unicodeKeyboard'] = 'true'
        proposal['resetKeyboard'] = 'true'
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)
        sleep(5)

    def get_toast_text(self, text):
        try:
            #toast_loc = (By.XPATH,"//*[contains(@text,'"+text+"')]".format(text))
            message = '//*[@text=\'{}\']'.format(text)
            #print(toast_loc)
            #ele = WebDriverWait(self.driver,15,0.1).until(expected_conditions.presence_of_element_located(toast_loc))
            toast_element = WebDriverWait(self.driver, 15, 0.1).until(lambda x: x.find_element_by_xpath(message))
            print(toast_element)
            return True

        except:
            return None
    def test_login(self):
        sleep(5)
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('spoedfjrhgpew')

        self.driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
        self.driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

        error_message = "账号不存在"
        #limit_message = "验证失败次数过多，请15分钟后再试"
        sleep(1)
        toast=self.get_toast_text("账号不存在")
        print(toast)

        # message = '//*[@text=\'{}\']'.format(error_message)
        # print(message)
        # # message='//*[@text=\'{}\']'.format(limit_message)
        #
        # toast_element = WebDriverWait(self.driver,15,0.1).until(lambda x: x.find_element_by_xpath(message))
        #
        # print(toast_element)
        # print(type(toast_element))




    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    #testunit.addTest(Test_case("test_login"))
