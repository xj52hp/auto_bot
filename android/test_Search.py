#-*- coding: UTF-8 -*-
import os
import unittest
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction



PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


class SearchAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='m1 note'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage']='com.ccvideo'
        #中文输入文本问题
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

        desired_caps['app'] = PATH('E:\\testpackage\\yzb.apk')#被测试的App在电脑上的位置

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_Search(self):
        time.sleep(5)
        try:
            #点击搜索按钮
            self.driver.find_element_by_id('com.ccvideo:id/tab_bar_search_btn').click()
            text = self.driver.find_element_by_id('com.ccvideo:id/tab_bar_keyword_et')
            text.click()
            text.send_keys("仲达")
            self.driver.find_element_by_id('com.ccvideo:id/tab_bar_cancel_tv').click()
            #进入其个人中心
            self.driver.find_element_by_id('com.ccvideo:id/title_layout').click()
            time.sleep(2)
            self.driver.back()
            #查看其视频
            self.driver.find_element_by_id('com.ccvideo:id/video_user_layout').click()
            time.sleep(5)
            self.driver.find_element_by_id('com.ccvideo:id/live_close_iv').click()
            #clear keyboard
            self.driver.find_element_by_id('com.ccvideo:id/clear_keyword_iv').click()
            #清空历史记录
            self.driver.find_element_by_id('com.ccvideo:id/clear_history_btn').click()
            self.driver.back()
        finally:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)