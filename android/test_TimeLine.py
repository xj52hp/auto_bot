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


class TimeLineAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        #desired_caps['device'] = '71UBBLD235NN'
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='m1 note'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage']='com.ccvideo'
        #desired_caps['appActivity']='com.yizhibo.video.activity.LoginMainActivity'
        #desired_caps['appActivity']='com.yizhibo.video.activity.HomeTabActivity'

        desired_caps['app'] = PATH('E:\\testpackage\\yzb.apk')#被测试的App在电脑上的位置

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_TimeLine(self):
        time.sleep(10)
        try:
            #进入时间轴
            self.driver.find_element_by_id('com.ccvideo:id/tab_timeline').click()
            #进入时间轴-回放
            self.driver.find_element_by_id('com.ccvideo:id/title_first_tv').click()
            time.sleep(2)
            #切换分类
            self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.ImageView[contains(@index,1)]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.ImageView[contains(@index,4)]").click()
            time.sleep(1)
            #进入回放视频观看
            self.driver.find_element_by_id('com.ccvideo:id/video_img').click()
            time.sleep(5)
            #点击饭团贡献榜
            self.driver.find_element_by_id('com.ccvideo:id/rice_roll_count_tv').click()
            time.sleep(2)
            self.driver.back()
            #点击分享
            self.driver.find_element_by_id('com.ccvideo:id/player_bottom_share_btn').click()
            self.driver.back()
            #点击进度条
            self.driver.find_element_by_id('com.ccvideo:id/player_bottom_progress_btn').click()
            self.driver.back()
            #点击礼物
            self.driver.find_element_by_id('com.ccvideo:id/live_gift_iv').click()
            self.driver.find_element_by_id('com.ccvideo:id/gift_iv').click()
            self.driver.find_element_by_id('com.ccvideo:id/send_gift_btn').click()
            #点击狂刷
            i = 0
            while i < 10:
                self.driver.find_element_by_id('com.ccvideo:id/burst_iv').click()
                i = i + 1
            #退出观看
            self.driver.find_element_by_id('com.ccvideo:id/live_close_iv').click()
            time.sleep(2)
            #点击现在
            self.driver.find_element_by_id('com.ccvideo:id/title_second_tv').click()
            #切换分类
            self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.ImageView[contains(@index,1)]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.ImageView[contains(@index,4)]").click()
            time.sleep(1)
            #观看直播
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView[0]/android.widget.RelativeLayout/android.widget.RelativeLayout").click()
            #点击预告
            self.driver.find_element_by_id('com.ccvideo:id/title_third_tv').click()
            time.sleep(2)
            #点击封面分享
            self.driver.find_element_by_id('com.ccvideo:id/live_notice_share_btn').click()
            self.driver.back()
            #点击封面删除
            self.driver.find_element_by_id('com.ccvideo:id/live_notice_delete_btn').click()
            self.driver.find_element_by_name("确定").click()

            self.driver.find_element_by_id('com.ccvideo:id/live_notice_thumb_iv').click()
            time.sleep(1)
            self.driver.find_element_by_id('com.ccvideo:id/live_notice_share_btn').click()
            self.driver.back()
            self.driver.back()
        finally:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TimeLineAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)