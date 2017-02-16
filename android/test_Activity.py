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


class ActivityAndroidTests(unittest.TestCase):
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

    def test_Activity(self):
        time.sleep(10)
        try:
            #进入活动
            self.driver.find_element_by_id('com.ccvideo:id/tab_activity').click()
            time.sleep(2)
            #点击活动封面进入活动详情页
            self.driver.find_element_by_id('com.ccvideo:id/activity_thumb_iv').click()
            time.sleep(1)
            #点击我要参与
            self.driver.find_element_by_id('com.ccvideo:id/activity_join_btn').click()
            time.sleep(2)
            #去掉蒙层
            #self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":100, "y":100})
            #去掉微信分享
            self.driver.find_element_by_id('com.ccvideo:id/share_weixin_circle_cb').click()
            #点击开始直播
            self.driver.find_element_by_id('com.ccvideo:id/live_start_btn').click()
            #黄赌毒提示
            #self.driver.find_element_by_id('android:id/button1').click()
            #录音权限允许
            #self.driver.find_element_by_id('android:id/button1').click()
            #去掉蒙层
            #self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":100, "y":100})
            time.sleep(15)
            #关闭直播
            self.driver.find_element_by_id('com.ccvideo:id/live_close_iv').click()
            #点击确定
            self.driver.find_element_by_id('android:id/button1').click()
            #保存视频
            self.driver.find_element_by_id('com.ccvideo:id/living_action_tv').click()
            time.sleep(2)
        finally:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ActivityAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)