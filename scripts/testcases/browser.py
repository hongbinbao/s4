#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d

class BrowserTest(unittest.TestCase):
    def setUp(self):
        super(BrowserTest, self).setUp()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.wakeup()
        d.press('back')\
         .press('back')\
         .press('home')

    def tearDown(self):
        super(BrowserTest, self).tearDown()
        d.press('back')\
         .press('back')\
         .press('back')\
         .press('home')

    def testOpenBrowser(self):
        assert d.exists(text='Internet') , 'Browser app not appear on the home screen'
        #assert d.exists(text='Apps')  , 'not appear on the home screen'
        d(text='Internet').click.wait()
        assert d(description="Bookmarks").wait.exists(timeout=10000), 'browser unable to open in 10 secs'
        d(className='android.widget.EditText').set_text('www.baidu.com')
        #d.click('go.png', threshold=0.01)
        d.press('enter')
        d.expect('baidu_logo.png', timeout=20)



