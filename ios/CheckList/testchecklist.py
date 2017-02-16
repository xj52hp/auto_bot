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

    # def test_checklist(self):
    #     # 首先验证注册登录页面中的协议部分
    #     self.test_protocol()
    #     # 之后是账号的登陆部分
    #     self.test_login()
    #     # 之后是活动轮播图部分，主要是其中的参与活动进行视频的录制
    #     self.test_carousel()
    #     # 之后是对于首页分类的操作，切换分类和不更改分类情况下直接完成
    #     self.test_classify()
    #     # 之后是预告部分的操作
    #     self.test_notice()

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
        # 点击登录进入欢迎登录页面
        # # *************微博登录成功之后退回到登录注册页面***************
        # self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]')
        # # 等待5秒实现页面出现
        # sleep(5)
        # # 第一次进入首页需要进行点击消除蒙层
        # self.driver.tap([(25, 42), ])
        # # 如果在审核状态下，app内存在广告，要关闭广告
        # self._closead()
        # # 进行账号退出
        # self._signout()
        # # 经验证，微博登录没有问题
        # logging.info("微博登录没有问题")
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
        self.driver.tap([(100, 100), ])
        # 信息输入完毕，点击登录按钮等待5秒实现页面出现
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')
        sleep(5)
        # 如果在审核状态下，app内存在广告，要关闭广告
        self._closead()
        # # 进行账号退出
        # self._signout()
        # 经验证，手机登录没有问题
        logging.info("手机登录没有问题")

    def _closead(self):
        # 点击每次登陆中间的广告
        self.driver.tap([(160, 280), ])
        # 点击右上角的关闭按钮消除广告
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]')

    def _signout(self):
        # 点击左上角头像进入个人中心
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        # 等5s等所有的元素都展示出来
        sleep(5)
        # 将页面进行上滑使得设置出现
        self.driver.swipe(160, 500, 160, 350, 400)
        # 获取设置按钮，并进行单击  
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[6]/UIAStaticText[1]')
        # 将页面进行上滑使得退出登录按钮出现
        self.driver.swipe(160, 500, 160, 200, 400)
        # 点击退出按钮。弹出退出确认按钮
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[12]')
        # 点击确定按钮进行退出账号
        self.actionElements('//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[1]')


    def test_carousel(self):
        sleep(5)
        # 如果在审核状态下，app内存在广告，要关闭广告
        self._closead()
        # -------------------------------------------------------------------------------------------------------
        #点击轮播图,进入轮播图的详情
        carouselbut = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIACollectionView[1]/UIACollectionView[1]')
        carouselbut.click()
        # 等待5s让所有元素展示出来
        sleep(5)
        # 获取标题确认不是广告
        activitytitlelabel = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]')
        activitytitle = activitytitlelabel.getText();
        activitybackbut = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]')
        # 判断标题内容是否是活动标题，若不是，返回之后重新进入
        while(self.assertNotEqual(activitytitle,'活动详情')):
            activitybackbut.click()
            sleep(5)
            carouselbut.click()
        # 当是活动详情时，不会进入循环,此时点击参与活动进行视频录制
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIAButton[1]')
        # 取消朋友圈分享
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[17]')
        # 点击开启直播进行视频录制
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[20]')
        # 点击中间消除蒙层,之后等待20s的视频录制
        self.driver.tap([(160, 280), ])
        sleep(20)
        # 点击视频关闭按钮
        liveclosebut = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[7]')
        liveclosebut.click()
        # 进行直播关闭确认
        self.actionElements('//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]/UIAButton[1]')
        # 进行视频保存
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[8]')
        # 视频保存之后返回到活动详情页，点击返回，返回到首页
        activitybackbut.click()

    def test_classify(self):
        # -------------------------------------------------------------------------------------------------------
        # 此部分进行对于首页分类的操作，切换分类和不更改分类情况下直接完成
        # 点击热门分类进入分类之中
        classifybut = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]')
        classifybut.click()
        # 切换一下不同的分类,选中第二个分类
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]')
        # 点击完成按钮完成分类切换
        finishbut = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')
        finishbut.click()
        # 等待3秒实现页面切换
        sleep(3)
        # 再次点击分类按钮进入分类详情页
        classifybut.click()
        # 不进行分类的更换，直接点击完成
        finishbut.click()

    def test_watchreplay(self):
        # -------------------------------------------------------------------------------------------------------
        # 此部分验证的是回放中的视频观看是否正常
        # 首先点击顶部的导航栏切换到回放部分
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[2]')
        # 等待两秒等待所有的元素展示出来
        sleep(2)
        # 点击第一个cell来进入回放
        self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAButton[2]')
        # 观看一下回放，观看时长一分钟
        sleep(60)
        # 关闭回放视频
        liveclosebut = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[7]')
        liveclosebut.click()

    def test_notice(self):
        # -------------------------------------------------------------------------------------------------------
        # 此部分验证预告
        # 首先点击顶部的导航栏切换到预告部分
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[4]')
        # 点击发布预告按钮,进入预告设置页
        self.driver.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIAButton[1]')
        # 首先向预告标题栏中输入内容
        noticetext = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]')
        noticetext.send_keys('壮哉兮吾辈之大道中国')
        # 更改设置直播时间
        changetime = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAPicker[1]/UIAPickerWheel[3]')
        # 将页面上滑使得元素时间至于最后
        self.driver.swipe(195, 280, 195, 160, 400)
        # 向预告详情中输入内容
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIATextView[1]')
        # 点击发布预告,发布之后需要2秒来等待发布成功
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIATextView[1]') 
        # 对第一个预告进行订阅
        subscribenotice = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]/UIAButton[3]')
        subscribenotice.click()
        # 订阅完成之后判断订阅是否变为了已订阅
        self.assertEqual(subscribenotice.getText(),'已订阅')
        # 点击封面进入预告详情
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]')
        # 对预告详情中的已关注和已订阅部分来比对
        attentionstatus = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAScrollView[1]/UIAButton[2]')
        self.assertEqual(attentionstatus.getText(),'已关注')
        subscribestatus = self.positionedElements('//UIAApplication[1]/UIAWindow[1]/UIAButton[6]')
        self.assertEqual(subscribestatus.getText(),'已订阅')
        # 点击返回按钮返回到预告页面
        self.actionElements('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]')


# 定义一个函数来保证测试用例的执行顺序
def suite():
    suite = unittest.TestSuite()
    suite.addTest(CheckListTests("test_protocol"))
    suite.addTest(CheckListTests("test_login"))
    # suite.addTest(CheckListTests("test_carousel"))
    # suite.addTest(CheckListTests("test_classify"))
    # suite.addTest(CheckListTests("test_notice"))
    return suite

if __name__ == '__main__':
    suite = suite()
    #执行测试
    unittest.TextTestRunner().run(suite)
