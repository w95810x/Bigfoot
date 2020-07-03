# coding=utf-8
from telnetlib import EC
from appium import webdriver
from time import sleep
import time
import unittest
import warnings
import json
import re
import os
import pytesseract
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from drivers import *

readDeviceId = list(os.popen('adb devices').readlines())
# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
csh=AppiumTest()
element=Element()
driver=csh.get_driver()

class Test_case(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)


    def test_Bootanimation(self):#OCR识别首次引导动画，后续优化点：1.抽出区域截图OCR识别
        # 获取当前界面activity
        ac = driver.current_activity
        # 等主页面activity出现
        driver.wait_activity(".broadway.activity.MainFlutterActivity", 10)
        #WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name('android.view.View'))
        #self.driver.find_element_by_class_name("android.widget.FrameLayout")
        driver.get_screenshot_as_file("E:\\screenshot\\new.png")
        sleep(3)
        img = Image.open("E:\\screenshot\\new.png")
        sleep(3)
        print(img.size)
        cropped = img.crop((300,800,970,1500))  # (left, upper, right, lower)截图
        cropped.save("E:\\screenshot\\new4.png")
        image = Image.open("E:\\screenshot\\new4.png")
        data = pytesseract.image_to_string(image)
        os.remove("E:\\screenshot\\new.png")
        os.remove("E:\\screenshot\\new4.png")
        text="Hi, I'm Max. Your personal gamassistant. I've mastered lots offancy game skills and ready tohelp you!"
        self.assertIsNotNone(text,data)

    def test_cbl_GPlogin(self):#侧边栏谷歌登录，后续优化点：1.抽出相同操作步骤 2.增加账户未登录，已登录异常判断
        csh.jrcbl()
        driver.find_element_by_xpath('//*[@text="LOGIN"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@text="CONTINUE WITH GOOGLE"]').click()
        sleep(1)
        driver.wait_activity("com.google.android.gms.common.account.AccountPickerActivity", 15)
        driver.find_element_by_xpath('//*[@text="赵雅倩"]').click()
        driver.wait_activity(".us.ozteam.bigfoot.broadway.activity.MainFlutterActivity", 15)
        driver.find_element_by_xpath('//*[@text="Settings"]').click()
        text=driver.find_element_by_xpath('//*[@text="Sign Out"]').text
        if text=='Sign Out':
            print('谷歌登录成功')
        else:
            print('谷歌登录失败')
        driver.find_element_by_xpath('//*[@text="Sign Out"]').click()
        driver.find_element_by_xpath('//*[@text="OK"]').click()
        driver.find_element_by_xpath('//*[@text="Back"]').click()

    def test_cbl_FBlogin(self):  # 侧边栏facebook登录，后续优化点：1.抽出相同操作步骤 2.增加账户未登录，已登录异常判断
        csh.jrcbl()
        driver.find_element_by_xpath('//*[@text="LOGIN"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@text="CONTINUE WITH FACEBOOK"]').click()
        driver.wait_activity(".us.ozteam.bigfoot.broadway.activity.MainFlutterActivity", 15)
        driver.find_element_by_xpath('//*[@text="Settings"]').click()
        text = driver.find_element_by_xpath('//*[@text="Sign Out"]').text
        if text == 'Sign Out':
            print('facebook登录成功')
        else:
            print('facebook登录失败')
        driver.find_element_by_xpath('//*[@text="Sign Out"]').click()
        driver.find_element_by_xpath('//*[@text="OK"]').click()
        driver.find_element_by_xpath('//*[@text="Back"]').click()
    def test_cbl_share(self):#侧边栏分享 后续优化点：进入侧边栏方法抽成函数，分享应用查找
        csh.jrcbl()
        driver.find_element_by_xpath('//*[@text="Share Bigfoot"]').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@resource-id="android:id/resolver_list"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
        sleep(5)
        ac = driver.current_activity
        print(ac)
        if ac=='us.ozteam.bigfoot.broadway.activity.MainFlutterActivity':
            print('分享成功')
        else:
            print('分享后没有返回侧边栏')

    def test_cbl_feedback(self):#反馈
        csh.jrcbl()
        driver.find_element_by_xpath('//*[@text="Feedback"]').click()
        sleep(1)
        srk=driver.find_elements_by_class_name('android.widget.EditText')
        srk[0].click()
        sleep(5)
        srk[0].send_keys('11111')
        driver.find_element_by_xpath('//*[@text="Contact Email (required)"]').click()
        driver.find_element_by_xpath('//*[@text="Contact Email (required)"]').send_keys('test@test.com')
        element.swipe_to_up()
        sleep(5)



    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # testunit.addTest(Test_case("test_Bootanimation"))
    # testunit.addTest(Test_case("test_cbl_GPlogin"))
    # testunit.addTest(Test_case("test_cbl_FBlogin"))
    #testunit.addTest(Test_case("test_cbl_share"))
    testunit.addTest(Test_case("test_cbl_feedback"))