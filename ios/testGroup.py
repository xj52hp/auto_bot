"""
不断进出直播间，是否会出现异常
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

class GroupTests(unittest.TestCase):

    logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='testlogin.log',
                filemode='w')

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

    def setUp(self):
        # set up appium
        app = os.path.abspath('/Users/APPLE/Desktop/安装包/oupai.ipa')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '7.1',
                'deviceName': 'iPhone 5'
            })

    def tearDown(self):
        self.driver.quit()

    def _closead(self):
        # 点击每次登陆中间的广告
        width = self.getPhoneWidth()
        height = self.getPhoneHeight()
        self.driver.tap([(width/2, height/2), ])
        # 点击右上角的关闭按钮消除广告
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]')

    def test_group(self):
        sleep(10)
        # 关闭广告
        self._closead()
        # 点击下方的导航栏进入消息页面
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[5]')
        # 等待两秒让所有的元素展示出来
        sleep(2)
        # 点击进入我的群组页面
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]')
        # 等待两秒让所有的元素展示出来
        sleep(2)
        # 点击一个群组，进入群组的资料页面
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]')
        while(True):
            # 点击添加成员
            self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]/UIAButton[5]')
            # 隐式等待3秒,捕捉元素
            self.driver.implicitly_wait(5)
            # 捕捉定位一下搜索栏
            search = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIATableCell[1]/UIATextField[2]')
            # 捕捉成功之后点击取消按钮来返回上一页再次进入进行循环
            self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]' )

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GroupTests)
    unittest.TextTestRunner(verbosity=2).run(suite)