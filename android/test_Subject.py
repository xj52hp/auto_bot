# -*- coding: UTF-8 -*-
import os
import unittest
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LiveAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'm1 note'  # 这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage'] = 'com.ccvideo'
        # 中文输入文本问题
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

        desired_caps['app'] = PATH('E:\\testpackage\\yzb.apk')  # 被测试的App在电脑上的位置

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_Subject(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver,5)
        try:
            # 进入话题页面
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/tab_activity')).click()
            # 点击轮播图
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/daimajia_slider_image')).click()
            self.driver.back()
            # 点击热门话题
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/subject_title_tv')).click()
            # 观看视频
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/video_img')).click()
            time.sleep(2)
            # 查看饭团榜
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/rice_roll_count_tv')).click()
            time.sleep(2)
            self.driver.back()
            # 点击进度条按钮
            # self.driver.find_element_by_id('com.ccvideo:id/player_bottom_progress_btn').click()
            self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":100, "y":100})
            # 礼物按钮
            self.driver.find_element_by_id('com.ccvideo:id/live_gift_iv').click()
            self.driver.find_element_by_id('com.ccvideo:id/gift_iv').click()
            self.driver.find_element_by_id('com.ccvideo:id/send_gift_btn').click()
            # 关闭按钮
            self.driver.find_element_by_id('com.ccvideo:id/live_close_iv').click()
            # 分享
            # wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/share_ll')).click()
            # QQ
            # wait.until(lambda x: x.find_element_by_xpath('//android.widget.GridView[1]/android.widget.LinearLayout[0]/android.widget.ImageView[contains(@index,0)]')).click()
            # 点赞
            self.driver.find_element_by_id('com.ccvideo:id/subject_love_iv').click()
            # 评论
            self.driver.find_element_by_id('com.ccvideo:id/subject_comment_iv').click()
            comment = self.driver.find_element_by_id('com.ccvideo:id/et_chat')
            comment.send_keys('asbnkdjnsalkdmslkmfd')
            self.driver.find_element_by_id('com.ccvideo:id/btn_send').click()
            # 查看点赞
            self.driver.find_element_by_id('com.ccvideo:id/tab_sub_like_ll').click()
            self.driver.back()
            #

        finally:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LiveAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)