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

    def test_Live(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver,5)
        try:
            # 点击直播按钮
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/tab_live')).click()
            # 进入直播设置页面
            # 设置分类
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'#颜控#')]").click()
            # 切换音频
            self.driver.find_element_by_id('com.ccvideo:id/live_pre_live_mode').click()
            # 切换视频
            self.driver.find_element_by_id('com.ccvideo:id/live_pre_live_mode').click()
            # 美颜按钮
            self.driver.find_element_by_id('').click()
            # 旋转镜头
            self.driver.find_element_by_id('com.ccvideo:id/live_cover_tv').click()
            # 设置封面
            self.driver.find_element_by_name("拍照").click()
            self.driver.find_element_by_id('com.ccvideo:id/live_set_thumb_camera_cb').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.ccvideo:id/live_ready_shoot_thumb_btn').click()
            # 设置标题
            title = self.driver.find_element_by_id('com.ccvideo:id/live_title_et')
            title.click()
            title.send_keys("瞅你咋滴！！")
            # 去掉朋友圈分享
            self.driver.find_element_by_id('com.ccvideo:id/share_weixin_circle_cb').click()
            # 设置权限
            self.driver.find_element_by_id('com.ccvideo:id/live_limit_cb').click()
            time.sleep(1)
            # 选择私密
            self.driver.find_element_by_name("私密").click()
            self.driver.find_element_by_name("完成").click()
            time.sleep(3)
            # 权限选择密码
            self.driver.find_element_by_id('com.ccvideo:id/live_limit_cb').click()
            time.sleep(1)
            self.driver.find_element_by_name("直播密码").click()
            self.driver.find_element_by_id('com.ccvideo:id/btn_two').click()
            self.driver.find_element_by_id('com.ccvideo:id/btn_five').click()
            self.driver.find_element_by_id('com.ccvideo:id/btn_eight').click()
            self.driver.find_element_by_id('com.ccvideo:id/btn_delete').click()
            self.driver.find_element_by_id('com.ccvideo:id/btn_eight').click()
            self.driver.find_element_by_id('com.ccvideo:id/btn_zero').click()
            self.driver.find_element_by_name("完成").click()
            time.sleep(3)
            # 权限选择好友可见
            self.driver.find_element_by_id('com.ccvideo:id/live_limit_cb').click()
            time.sleep(1)
            self.driver.find_element_by_name("好友可见").click()
            self.driver.find_element_by_name("完成").click()
            time.sleep(3)
            # 权限选择部分好友可见
            self.driver.find_element_by_id('com.ccvideo:id/live_limit_cb').click()
            time.sleep(1)
            self.driver.find_element_by_name("部分好友可见").click()
            self.driver.find_element_by_id('com.ccvideo:id/allow_cb').click()
            self.driver.find_element_by_name("完成").click()
            time.sleep(3)
            # 权限选择公开
            self.driver.find_element_by_id('com.ccvideo:id/live_limit_cb').click()
            time.sleep(1)
            self.driver.find_element_by_name("公开").click()
            self.driver.find_element_by_name("完成").click()
            time.sleep(3)
            # 关闭位置
            self.driver.find_element_by_id('com.ccvideo:id/live_gps_cb').click()
            # 开始直播
            self.driver.find_element_by_id('com.ccvideo:id/live_start_btn').click()
            time.sleep(3)
            # 更多设置
            self.driver.find_element_by_id('com.ccvideo:id/live_options_right_arrow_iv').click()
            # 修改标题
            self.driver.find_element_by_name("标题").click()
            title = self.driver.find_element_by_class_name('android.widget.EditText')
            title.click()
            title.send_keys("heihei")
            self.driver.find_element_by_name("确定").click()
            # 修改分类
            self.driver.find_element_by_name("分类").click()
            self.driver.find_element_by_name("陪我").click()
            # 静音
            self.driver.find_element_by_id('com.ccvideo:id/live_mute_cb').click()
            # 关闭更多设置
            self.driver.find_element_by_id('com.ccvideo:id/live_options_left_arrow_iv').click()
            # 评论
            self.driver.find_element_by_id('com.ccvideo:id/live_comment_iv').click()
            self.driver.find_element_by_id('com.ccvideo:id/rl_input').send_keys("heihei")
            self.driver.find_element_by_name("发送").click()
            # 发送红包
            self.driver.find_element_by_id('com.ccvideo:id/live_send_red_pack_iv').click()
            # 设置红包个数
            red_pac_num = self.driver.find_element_by_id('com.ccvideo:id/red_pack_number_et')
            red_pac_num.click()
            red_pac_num.send_keys("5")
            # 设置易币数
            e_coin_num = self.driver.find_element_by_id('com.ccvideo:id/e_coin_number_et')
            e_coin_num.click()
            e_coin_num.send_keys("10")
            # 设置红包标题
            red_pac_mes = self.driver.find_element_by_id('com.ccvideo:id/red_pack_message_et')
            red_pac_mes.click()
            red_pac_mes.send_keys("低调的无内涵")
            # 点击发送
            self.driver.find_element_by_id('com.ccvideo:id/btn_send_red_pack_tv').click()
            time.sleep(3)
            # 抢红包
            self.driver.find_element_by_id('')
            # self.driver.find_element_by_id('com.ccvideo:id/close_iv').click()
            # 分享
            self.driver.find_element_by_id('com.ccvideo:id/live_share_iv').click()
            self.driver.find_element_by_id('com.ccvideo:id/bs_list_image').click()
            time.sleep(5)
            self.driver.find_element_by_id('com.sina.weibo:id/titleSave').click()
            # 关闭直播
            self.driver.find_element_by_id('com.ccvideo:id/live_close_iv').click()
            self.driver.find_element_by_name("确定").click()
            # 回放
            self.driver.find_element_by_id('com.ccvideo:id/lep_left_tv').click()
            time.sleep(4)
            self.driver.back()
            # 保存
            self.driver.find_element_by_id('com.ccvideo:id/living_action_tv').click()
        finally:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LiveAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
