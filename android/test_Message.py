#-*- coding: UTF-8 -*-
import os
import unittest
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait


PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


class MessageAndroidTests(unittest.TestCase):
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

    def test_Message(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver,5)
        try:
            #点击进入消息
            self.driver.find_element_by_id('com.ccvideo:id/tab_message').click()
            time.sleep(1)
            #去掉蒙层
            self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":100, "y":100})
            #点击新朋友
            self.driver.find_element_by_id('com.ccvideo:id/msg_logo_iv').click()
            self.driver.back()
            #点击易直播小秘书
            self.driver.find_element_by_id('com.ccvideo:id/msg_title_tv').click()
            self.driver.back()
            #点击加号
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/add_option_iv')).click()
            #发起群聊
            self.driver.find_element_by_name("发起群聊").click()
            #选择好友
            i = 0
            while i < 3:
                self.driver.find_element_by_id('com.ccvideo:id/user_item_ll').click()
                i = i + 1
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'完成')]").click()
            #进入群聊页面
            #发送评论
            mes = wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/et_sendmessage'))
            mes.click()
            mes.send_keys("哦四季度卡i温暖的考虑为")
            self.driver.find_element_by_name("发送").click()
            #发送语音
            self.driver.find_element_by_id('com.ccvideo:id/btn_set_mode_voice').click()
            voice = self.driver.find_element_by_name("按住说话")
            action1 = TouchAction(self.driver)
            action1.long_press(voice).wait(4000).perform()
            #选择更多
            self.driver.find_element_by_id('com.ccvideo:id/btn_more').click()
            #发送视频
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/btn_video')).click()
            #设置分类
            # self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'#颜控#')]").click()
            #切换音频
            self.driver.find_element_by_id('com.ccvideo:id/live_pre_live_mode').click()
            #切换视频
            self.driver.find_element_by_id('com.ccvideo:id/live_pre_live_mode').click()
            #旋转镜头
            self.driver.find_element_by_id('com.ccvideo:id/live_cover_tv').click()
            self.driver.find_element_by_name("拍照").click()
            self.driver.find_element_by_id('com.ccvideo:id/live_set_thumb_camera_cb').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.ccvideo:id/live_ready_shoot_thumb_btn').click()
            #开始直播
            self.driver.find_element_by_id('com.ccvideo:id/live_start_btn').click()
            #更多设置
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/live_options_right_arrow_iv')).click()
            #修改标题
            self.driver.find_element_by_name("标题").click()
            title = self.driver.find_element_by_class_name('android.widget.EditText')
            title.click()
            title.send_keys("heihei")
            self.driver.find_element_by_name("确定").click()
            #修改分类
            self.driver.find_element_by_name("分类").click()
            self.driver.find_element_by_name("美女").click()
            #静音
            self.driver.find_element_by_id('com.ccvideo:id/live_mute_cb').click()

            self.driver.find_element_by_id('com.ccvideo:id/live_options_left_arrow_iv').click()
            #评论
            self.driver.find_element_by_id('com.ccvideo:id/live_comment_iv').click()
            self.driver.find_element_by_id('com.ccvideo:id/rl_input').send_keys("heihei")
            self.driver.find_element_by_name("发送").click()
            #分享
            self.driver.find_element_by_id('com.ccvideo:id/live_share_iv').click()
            self.driver.back()
            #关闭直播
            self.driver.find_element_by_id('com.ccvideo:id/live_close_iv').click()
            self.driver.find_element_by_name("确定").click()
            #回放
            # self.driver.find_element_by_id('com.ccvideo:id/lep_left_tv').click()
            # time.sleep(6)
            # self.driver.back()
            #保存
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/living_action_tv')).click()
            #拍照
            self.driver.find_element_by_id('com.ccvideo:id/btn_take_picture').click()
            self.driver.find_element_by_id('com.meizu.media.camera:id/shutter_btn').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.meizu.media.camera:id/btn_done').click()
            #发送图片
            self.driver.find_element_by_id('com.ccvideo:id/btn_picture').click()
            self.driver.find_element_by_id('com.meizu.media.gallery:id/thumbnail_check_box').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.meizu.media.gallery:id/action_get_multi_confirm').click()
            #发送位置
            self.driver.find_element_by_id('com.ccvideo:id/btn_location').click()
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/menu_send')).click()
            #查看资料
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/user_info_btn')).click()
            time.sleep(1)
            #修改群名
            self.driver.find_element_by_id('com.ccvideo:id/group_name_change_tv').click()
            gname = self.driver.find_element_by_id('com.ccvideo:id/change_group_name')
            gname.click()
            gname.send_keys("战无不胜")
            self.driver.find_element_by_name("完成").click()
            #查看群成员
            self.driver.find_element_by_id('com.ccvideo:id/group_member_number_tv').click()
            self.driver.back()
            #添加群成员
            self.driver.find_element_by_id('com.ccvideo:id/add_member_iv').click()
            self.driver.find_element_by_id('com.ccvideo:id/user_item_ll').click()
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'完成')]").click()
            #删除群成员
            self.driver.find_element_by_id('com.ccvideo:id/sub_member_iv').click()
            self.driver.find_element_by_id('com.ccvideo:id/allow_cb').click()
            self.driver.find_element_by_id('com.ccvideo:id/menu_delete').click()
            #清空聊天记录
            self.driver.find_element_by_id('com.ccvideo:id/group_clean_history_ll').click()
            #举报群组
            self.driver.find_element_by_id('com.ccvideo:id/report_group_ll').click()
            self.driver.find_element_by_name("违法信息")
            #群公告

            #解散该群
            self.driver.find_element_by_id('com.ccvideo:id/dissolution_group_tv').click()

            #群组页面建群
            wait.until(lambda x: x.find_element_by_id('com.ccvideo:id/menu_add_group')).click()
            self.driver.find_element_by_id('com.ccvideo:id/user_item_ll').click()
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'完成')]").click()
        finally:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MessageAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)