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


class TaCenterAndroidTests(unittest.TestCase):
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

    def test_TaCenter(self):
        time.sleep(5)
        try:
            #进入个人中心
            PersonCenter = self.driver.find_element_by_id('com.ccvideo:id/tab_bar_mine_btn')
            PersonCenter.click()
            time.sleep(2)
            #进入粉丝列表
            self.driver.find_element_by_id('com.ccvideo:id/fans_count_tv').click()
            time.sleep(2)
            #进入他人个人中心
            self.driver.find_element_by_id('com.ccvideo:id/title_layout').click()
            time.sleep(2)
            #改变关注状态
            self.driver.find_element_by_id('com.ccvideo:id/operation_action_iv').click()
            #修改备注
            self.driver.find_element_by_id('com.ccvideo:id/mine_set_remarks_tv').click()
            remark = self.driver.find_element_by_id('com.ccvideo:id/remark_remarks_et')
            remark.click()
            remark.send_keys("哼哼哈嘿")
            self.driver.find_element_by_id('com.ccvideo:id/menu_commit').click()
            #观看视频
            self.driver.find_element_by_id('com.ccvideo:id/mv_video_logo_iv').click()
            self.driver.back()
            #粉丝列表
            self.driver.find_element_by_id('com.ccvideo:id/fans_count_tv').click()
            self.driver.back()
            #关注列表
            self.driver.find_element_by_id('com.ccvideo:id/follow_count_tv').click()
            self.driver.back()
            #私信
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'私信')]").click()
            time.sleep(2)
            #发送评论
            mes = self.driver.find_element_by_id('com.ccvideo:id/et_sendmessage')
            mes.click()
            mes.send_keys("哦四季度卡i温暖的考虑为")
            self.driver.find_element_by_name("发送").click()
            #发送语音
            self.driver.find_element_by_id('com.ccvideo:id/btn_set_mode_voice').click()
            voice = self.driver.find_element_by_name("按住说话")
            action1 = TouchAction(self.driver)
            action1.long_press(voice).wait(4000).perform()
            time.sleep(2)
            #选择更多
            self.driver.find_element_by_id('com.ccvideo:id/btn_more').click()
            #发送视频
            self.driver.find_element_by_id('com.ccvideo:id/btn_video').click()
            time.sleep(3)
            #设置分类
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'#颜控#')]").click()
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
            self.driver.find_element_by_id('com.ccvideo:id/live_options_right_arrow_iv').click()
            #修改标题
            self.driver.find_element_by_name("标题").click()
            title = self.driver.find_element_by_class_name('android.widget.EditText')
            title.click()
            title.send_keys("heihei")
            self.driver.find_element_by_name("确定").click()
            #修改分类
            self.driver.find_element_by_name("分类").click()
            self.driver.find_element_by_name("陪我").click()
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
            self.driver.find_element_by_id('com.ccvideo:id/lep_left_tv').click()
            time.sleep(4)
            self.driver.back()
            #保存
            self.driver.find_element_by_id('com.ccvideo:id/living_action_tv').click()
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
            time.sleep(2)
            self.driver.find_element_by_id('com.ccvideo:id/menu_send').click()
            time.sleep(2)
            #返回
            self.driver.back()
            #拉黑
            self.driver.find_element_by_id('com.ccvideo:id/pull_black_tv').click()
            self.driver.find_element_by_name("确定").click()
            time.sleep(3)
            #解除拉黑
            self.driver.find_element_by_id('com.ccvideo:id/pull_black_tv').click()
            time.sleep(3)
        finally:
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            os.popen("adb pull /data/local/tmp/tmp.png E:\\Dev_Root\\python\\how_to_dev_python\\autobot\\android\\screenshot"  + "\\" + timestamp + ".png")
            time.sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TaCenterAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)