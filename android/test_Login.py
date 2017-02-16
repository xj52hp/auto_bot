    #-*- coding: UTF-8 -*-
import os
import unittest
import time
import traceback

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        #desired_caps['device'] = '71UBBLD235NN'
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='m1 note'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage']='com.ccvideo'
        #desired_caps['appActivity']='com.yizhibo.video.activity.LoginMainActivity'
        #desired_caps['appActivity']='com.yizhibo.video.activity.HomeTabActivity'
        # #中文输入文本问题
        # desired_caps["unicodeKeyboard"] = "True"
        # desired_caps["resetKeyboard"] = "True"

        desired_caps['app'] = PATH('E:\\testpackage\\yzb.apk')#被测试的App在电脑上的位置

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        time.sleep(10)
        try:
            # 获取手机屏幕分辨率
            width = self.driver.get_window_size()['width']

            height = self.driver.get_window_size()['height']

            width = int(width*0.1)
            height = int(height*0.1)


            # 滑动屏幕
            self.driver.swipe(900,900,100,900,1000)
            sleep(1)
            self.driver.swipe(900,900,100,900,1000)
            sleep(1)
            #点击进入
            enter = self.driver.find_element_by_id('com.ccvideo:id/press_enter_btn')
            enter.click()

            time.sleep(10)

            # 登录
            login = self.driver.find_element_by_id('com.ccvideo:id/go_login_btn')
            self.assertIsNotNone(login)
            login.click()

            # 输入账号

            name = self.driver.find_element_by_id('com.ccvideo:id/register_phone_et')
            self.assertIsNotNone(name)
            name.click()
            name.send_keys('17600804696')

            title = self.driver.find_element_by_id('com.ccvideo:id/login_title_tv')
            title.click()

           # 输入密码
            psd = self.driver.find_element_by_id('com.ccvideo:id/password_et')
            self.assertIsNotNone(psd)
            psd.click()
            psd.send_keys('123456')

            title = self.driver.find_element_by_id('com.ccvideo:id/login_title_tv')
            title.click()

            # 点击登录按钮
            blogin = self.driver.find_element_by_id('com.ccvideo:id/login_btn')
            self.assertIsNotNone(blogin)
            blogin.click()
        finally:
            # 检测到异常后截屏并发送至电脑指定目录下
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)

        self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":100, "y":100})

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)