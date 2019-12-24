# ecoding=utf-8
import re
import json
# 使用time.sleep(xx)函数进行等待
import warnings
import sys
from importlib import reload
reload(sys)
from time import sleep
# 使用 os 模块调用命令
import os
# 读取设备 id
from appium.webdriver.mobilecommand import MobileCommand

readDeviceId = list(os.popen('adb devices').readlines())
# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
from appium import webdriver
class AppiumTest:
    def __init__(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': deviceAndroidVersion,
                        'deviceName': deviceId,
                        'automationName':'uiautomator2',
                        'unicodeKeyboard':'true',
                        'resetKeyboard':'true',
                        'appPackage': 'us.ozteam.bigfoot',
                        'appActivity': 'us.ozteam.bigfoot.broadway.activity.MainFlutterActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)


    def get_driver(self):
        return self.driver
    def jrcbl(self):
        sleep(10)
        # 获取当前界面activity
        ac = self.driver.current_activity
        print(ac)
        # 等主页面activity出现
        self.driver.wait_activity(".broadway.activity.MainFlutterActivity", 10)
        self.driver.find_element_by_class_name("android.view.View").click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@resource-id="android:id/content"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[1]').click()
        sleep(1)
class Element:
    """
    封装Appium中关于元素对象的方法
    """

    def __init__(self):
        at = AppiumTest()
        self.driver = at.get_driver()

    def get_id(self, id):
        element = self.driver.find_element_by_id(id)
        return element

    def get_name(self, name):
        element = self.driver.find_element_by_name(name)
        return element

    def over(self):
        element = self.driver.quit()
        return element

    def get_screen(self, path):
        self.driver.get_screenshot_as_file(path)

    def get_size(self):
        size = self.driver.get_window_size()
        return size

    def swipe_to_up(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_to_down(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_to_left(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_to_right(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def back(self):
        self.driver.keyevent(4)

    def get_classes(self, classesname):
        elements = self.driver.find_elements_by_class_name(classesname)
        return elements

    def get_ids(self, ids):
        elements = self.driver.find_elements_by_id(ids)
        return elements

    def switch_h5(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.weizq"})

    def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})

command0 ='adb shell ime list -s'
command1 ='adb shell settings get secure default_input_method'
command2 ='adb shell ime set com.sec.android.inputmethod/.SamsungKeypad'
command3 ='adb shell ime set io.appium.settings/.UnicodeIME'

# 列出系统现在所安装的所有输入法
#os.system(command0)
# 打印系统当前默认的输入法
#os.system(command1)
# 切换latin输入法为当前输入法
#os.system(command2)
# 切换appium输入法为当前输入法
#os.system(command3)

class InputMethod:

    # 切换latin输入法为当前输入法
    def enableLatinIME(self):
        os.system(command2)

    # 切换appium输入法为当前输入法
    def enableAppiumUnicodeIME(self):
        os.system(command3)