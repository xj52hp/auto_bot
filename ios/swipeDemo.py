"""
解决swipe在ios设备上操作出错的问题，利用分辨率来进行解决，分辨率设置全局使用变量
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

class CircleLiveTests(unittest.TestCase):

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
        self.driver.tap([(160, 280), ])
        # 点击右上角的关闭按钮消除广告
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]')

    def test_circleinoutlive(self):
        sleep(10)
        # 关闭广告
        self._closead()
        width = self.getPhoneWidth()
        height = self.getPhoneHeight()
        p1 = int(width/2)
        p2 = int(height*0.6)
        p3 = p1
        p4 = int(height*0.5)

        self.driver.swipe(start_x=p1, start_y=p2, end_x=p3, end_y=p4, duration=500)
        sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CircleLiveTests)
    unittest.TextTestRunner(verbosity=2).run(suite)