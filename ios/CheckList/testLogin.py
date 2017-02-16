#!/bin/python
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class CheckListTests(unittest.TestCase):

    logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='testlogin.log',
                filemode='w')

    def setUp(self):
        # set up appium
        app = os.path.abspath('/Users/APPLE/Desktop/安装包/oupai.ipa')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '8.0.2',
                'deviceName': 'iPhone 5s'
            })

    def tearDown(self):
        self.driver.quit()

    def getPhoneWidth(self):
        # 获取手机的分辨率(iphone5和5s为例，width=320,height=568)
        width = self.driver.get_window_size()['width']
        return width

    def getPhoneHeight(self):
        height = self.driver.get_window_size()['height']
        return height

    # 元素定位的函数表示
    def positionedElements(self, path):
        elements = self.driver.find_element_by_xpath(path)
        return elements

    # 元素定位之后，并且进行元素的点击产生效果
    def actionElements(self,path):
        elements = self.driver.find_element_by_xpath(path)
        elements.click()

    def test_protocol(self):
        sleep(5)
        # 首先进入的是登录注册页面
        # 点击注册进入注册页面
        # -------------------------------------------------------------------------------------------------------
        registerbut = self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')
        # 验证服务条款后返回
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[3]/UIALink[1]')
        protocolcontent = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIATextView[1]')
        # 验证服务条款的文本
        if not "用户注册协议" in protocolcontent.text:
            raise TextError('服务条款文本错误')
        else:
            pass
        # 点击返回按钮
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        # backbut = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        # backbut.click()
        # 同样方法验证一轮隐私协议
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[3]/UIALink[2]')
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        # 点击叉号回到登录注册页面
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]')
        # 验证协议部分成功
        logging.info("注册页面中的服务条款、隐私协议没有问题")
    
    def test_login(self):
        # -------------------------------------------------------------------------------------------------------
        # 手机号码和第三方账号登录
        width = self.getPhoneWidth()
        height = self.getPhoneHeight()
        # 点击登录进入欢迎登录页面
        # *************微博登录成功之后退回到登录注册页面***************
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]')
        # 等待5秒实现页面出现
        sleep(5)
        # 第一次进入首页需要进行点击消除蒙层
        self.driver.tap([(int(width/10), int(height/10)), ])
        # 如果在审核状态下，app内存在广告，要关闭广告
        self._closead()
        # 进行账号退出
        self._signout()
        # 经验证，微博登录没有问题
        logging.info("微博登录没有问题")
        # # *************微信登录成功之后退回到登录注册页面***************
        # self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[4]')
        # # 等待5秒实现页面出现
        # sleep(5)
        # self._closead()
        # # 进行账号退出
        # self._signout()
        # # 经验证，微信登录没有问题
        # logging.info("微信登录没有问题")
        # # *************微信登录成功之后退回到登录注册页面***************
        # self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[5]')
        # # 等待5秒实现页面出现
        # sleep(5)
        # self._closead()
        # # 进行账号退出
        # self._signout()
        # # 经验证，QQ登录没有问题
        # logging.info("QQ登录没有问题")
        # *************手机登录成功之后退回到登录注册页面***************
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        # 输入正确数据正常登录 手机号码13784975654 密码111111
        phonenum = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]')
        phonenum.send_keys('13784975654')
        password = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]')
        password.send_keys('111111')
        # 点击顶端把键盘清除
        self.driver.tap([(int(width*0.31), int(height*0.18)), ])
        # 信息输入完毕，点击登录按钮等待5秒实现页面出现
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')
        sleep(5)
        # # 如果在审核状态下，app内存在广告，要关闭广告
        # self._closead()
        # # 进行账号退出
        self._signout()
        # 经验证，手机登录没有问题
        logging.info("手机登录没有问题")

    def _closead(self):
        width = self.getPhoneWidth()
        height = self.getPhoneHeight()
        self.driver.tap([(width/2, height/2), ])
        # 点击右上角的关闭按钮消除广告
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]')

    def _signout(self):
        width = self.getPhoneWidth()
        height = self.getPhoneHeight()
        # 点击左上角头像进入个人中心
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        # 等5s等所有的元素都展示出来
        self.driver.implicitly_wait(10)
        # 设置滑动坐标
        p1 = int(width/2)
        p2 = int(height*0.6)
        p3 = p1
        p4 = int(height*0.4)
        # 将页面进行上滑使得设置出现
        self.driver.swipe(start_x=p1, start_y=p2, end_x=p3, end_y=p4, duration=500)
        # 获取设置按钮，并进行单击  
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[6]/UIAStaticText[1]')
        # 将页面进行上滑使得退出登录按钮出现
        self.driver.swipe(start_x=p1, start_y=p2, end_x=p3, end_y=p4, duration=500)
        # 点击退出按钮。弹出退出确认按钮
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[12]')
        # 点击确定按钮进行退出账号
        self.actionElements('//UIAApplication[1]/UIAWindow[3]/UIAAlert[1]/UIATableView[1]/UIATableCell[1]')


# 定义一个函数来保证测试用例的执行顺序
def suite():
    suite = unittest.TestSuite()
    suite.addTest(CheckListTests("test_protocol"))
    suite.addTest(CheckListTests("test_login"))
    return suite

if __name__ == '__main__':
    suite = suite()
    #执行测试
    unittest.TextTestRunner().run(suite)
