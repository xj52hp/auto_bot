# -*- coding: UTF-8 -*-
import os
import unittest
import sys, time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class PersonCenterAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        # desired_caps['device'] = '71UBBLD235NN'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'm1 note'  # 这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage'] = 'com.ccvideo'

        desired_caps['app'] = PATH('E:\\testpackage\\yzb.apk')  # 被测试的App在电脑上的位置

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_Personcenter(self):
        time.sleep(10)
        wait = WebDriverWait(self.driver,5)
        try:
            # 个人中心
            PersonCenter = wait.until(lambda x:x.find_element_by_id('com.ccvideo:id/tab_bar_mine_btn'))
            PersonCenter.click()
            # time.sleep(2)
            # 去掉蒙层
            # self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":100, "y":100})
            # 分享个人中心
            wait.until(lambda x:x.find_element_by_id('com.ccvideo:id/operation_action_iv')).click()
            self.driver.back()
            # QQ分享
            # QQ = self.driver.find_element_by_xpath("//android.widget.FrameLayout[0]/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[0]/android.widget.ImageView[contains(@index,0)]")
            # 设置个人资料
            edit = self.driver.find_element_by_name("编辑资料")
            edit.click()
            time.sleep(2)
            # edittext = self.driver.find_element_by_class_name("android.widget.EditText")
            # edittext[0].send_keys("Rtian Zhao")
            # edittext[2].send_keys("heihei")

            # self.assertEqual("且听风吟我就试一试",edittext[0].text)
            # self.assertEqual("Ta太聪明了，忘了自绍了！",edittext[2].text)

            self.driver.find_element_by_name("完成").click()
            # 滑动背景
            # self.driver.swipe(900, 900, 100, 900, 1000)

            # 进入视频列表
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'视频')]").click()
            time.sleep(4)
            # 去掉蒙层
            # self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":100, "y":100})
            # 视频设置
            wait.until(lambda x:x.find_element_by_id('com.ccvideo:id/my_video_set_iv')).click()
            self.driver.find_element_by_name("标题编辑").click()
            # edittext = self.driver.find_element_by_class_name("android.widget.EditText")
            # edittext[0].send_keys("Rtian")
            self.driver.find_element_by_name("确定").click()
            # 返回上一页
            self.driver.back()

            # 进入赚薏米
            self.driver.find_element_by_id('com.ccvideo:id/item_make_rice_rl').click()
            time.sleep(2)
            # 点击领取
            # self.driver.find_element_by_id('com.ccvideo:id/task_rice_receive_tv').click()
            # 点击签到
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/sign_in_btn')).click()
            # 点击说明
            wait.until(lambda x: x.find_element_by_name("薏米相关说明")).click()
            # 返回上一页
            self.driver.back()
            self.driver.back()

            # 进入我的等级
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/item_my_level_rl')).click()
            self.driver.back()

            # 进入易币充值
            self.driver.find_element_by_id('com.ccvideo:id/item_cash_in_rl').click()
            time.sleep(1)
            # 查看充值记录
            wait.until(lambda x: x.find_element_by_name("充值记录")).click()
            self.driver.back()
            self.driver.back()

            # 进入我的收益
            self.driver.find_element_by_id('com.ccvideo:id/item_my_profit_rl').click()
            time.sleep(1)
            # 查看提现记录
            self.driver.find_element_by_name("提现记录").click()
            self.driver.back()
            # 进入兑换页面
            self.driver.find_element_by_id('com.ccvideo:id/money_exchange_btn').click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//android.widget.CheckBox[contains(@text,'￥ 10')]").click()
            # self.driver.find_element_by_id('com.ccvideo:id/exchange_money_tv').click()
            self.driver.find_element_by_id('com.ccvideo:id/exchange_money_submit_btn').click()
            time.sleep(2)
            # 提现
            self.driver.find_element_by_id('com.ccvideo:id/rise_cash_btn').click()
            self.driver.back()
            self.driver.back()

            # 邀请好友
            self.driver.find_element_by_id('com.ccvideo:id/item_add_friend_rl').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.ccvideo:id/interested_friends').click()
            time.sleep(2)
            # self.driver.find_element_by_id('com.ccvideo:id/follow_cb').click()
            self.driver.back()
            self.driver.find_element_by_id('com.ccvideo:id/nearby_friends').click()
            self.driver.back()
            self.driver.back()

            # 设置
            # self.driver.swipe(727,1621,727,1400,1000)
            self.driver.find_element_by_id('com.ccvideo:id/item_message_notice_rl').click()
            time.sleep(1)
            # 点击三个通知
            self.driver.find_element_by_id('com.ccvideo:id/notice_follow_event_cb').click()
            self.driver.find_element_by_id('com.ccvideo:id/notice_chat_event_cb').click()
            self.driver.find_element_by_id('com.ccvideo:id/notice_all_cb').click()
            # 点击直播消息提醒
            self.driver.find_element_by_id('com.ccvideo:id/notice_push_message_setting_rl').click()
            time.sleep(1)
            self.driver.find_element_by_id('com.ccvideo:id/location_toggle_tb').click()
            self.driver.back()
            # 点击账号管理
            self.driver.find_element_by_id('com.ccvideo:id/account_bind_arrow_iv').click()
            self.driver.back()
            # 点击黑名单
            self.driver.find_element_by_id('com.ccvideo:id/blacklist_iv').click()
            time.sleep(1)
            self.driver.find_element_by_name("解除").click()
            self.driver.back()
            # 点击关于
            self.driver.find_element_by_id('com.ccvideo:id/about_us_arrow_iv').click()
            time.sleep(1)
            self.driver.find_element_by_id('com.ccvideo:id/about_us_rl').click()
            self.driver.back()
            # self.driver.find_element_by_id('com.ccvideo:id/contact_us_rl').click()
            # self.driver.back()
            self.driver.find_element_by_id('com.ccvideo:id/seizure_account_rl').click()
            self.driver.back()
            self.driver.find_element_by_id('com.ccvideo:id/copyright_rl').click()
            self.driver.back()
            self.driver.find_element_by_id('com.ccvideo:id/manual_check_update_rl')
            time.sleep(2)
            self.driver.find_element_by_id('com.ccvideo:id/feedback_rl').click()
            # 意见反馈
            content = self.driver.find_element_by_id('com.ccvideo:id/umeng_fb_send_content')
            content.send_keys("sndk")
            self.driver.find_element_by_id('com.ccvideo:id/umeng_fb_send_btn').click()
            time.sleep(2)
            self.driver.back()
            self.driver.back()
            self.driver.back()

            # 退出登录
            self.driver.find_element_by_id('com.ccvideo:id/logout_btn').click()
            self.driver.find_element_by_id('android:id/button2').click()
            self.driver.back()
            self.driver.back()
        finally:
            # 检测到异常后截屏并发送至电脑指定目录下
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PersonCenterAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
