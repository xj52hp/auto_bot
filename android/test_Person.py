#-*- coding: UTF-8 -*-
import os
import unittest
import sys,time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


class PersonAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        #desired_caps['device'] = '71UBBLD235NN'
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='m1 note'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage']='com.ccvideo'
        #desired_caps['appActivity']='com.yizhibo.video.activity.LoginMainActivity'
        #desired_caps['appActivity']='com.yizhibo.video.activity.HomeTabActivity'
        #中文输入文本问题
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

        desired_caps['app'] = PATH('E:\\testpackage\\yzb.apk')#被测试的App在电脑上的位置

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_Person(self):
        time.sleep(10)
        try:
            #进入找朋友
            self.driver.find_element_by_id('com.ccvideo:id/tab_person').click()
            #进入排行
            self.driver.find_element_by_id('com.ccvideo:id/title_first_tv').click()
            time.sleep(1)
            #点击查看更多
            self.driver.find_element_by_id('com.ccvideo:id/ranking_more_tv').click()
            time.sleep(5)
            #进入个人中心
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'永远的追风3号')]").click()
            time.sleep(2)
            self.driver.back()
            self.driver.back()

            #点击月榜
            self.driver.find_element_by_id('com.ccvideo:id/now_middle_btn').click()
            time.sleep(2)
            #点击总榜
            self.driver.find_element_by_id('com.ccvideo:id/now_right_btn').click()
            time.sleep(2)

            #进入关注
            self.driver.find_element_by_id('com.ccvideo:id/title_second_tv').click()
            time.sleep(1)
            #点击头像
            self.driver.find_element_by_id('com.ccvideo:id/my_user_photo').click()
            time.sleep(3)
            self.driver.back()
            #点击视频封面
            self.driver.find_element_by_id('com.ccvideo:id/itf_screenshot_iv').click()
            time.sleep(3)
             #退出观看
            self.driver.find_element_by_id('com.ccvideo:id/live_close_iv').click()
            time.sleep(3)

            #进入频道
            self.driver.find_element_by_id('com.ccvideo:id/title_third_tv').click()
            time.sleep(1)
            #点击频道封面
            self.driver.find_element_by_id('com.ccvideo:id/title_tv').click()
            time.sleep(1)
            self.driver.back()
        finally:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PersonAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)