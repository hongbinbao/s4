#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest, self).setUp()
        d.wakeup()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.press('back')\
         .press('back')\
         .press('home')

    def tearDown(self):
        super(CameraTest, self).tearDown()
        d.press('back')\
         .press('back')\
         .press('back')\
         .press('home')

    def testTakePicture(self):
        assert d.exists(text='Camera') , 'camera app not appear on home screen'
        #assert d.exists(text='Apps')
        d(text='Camera').click.wait()
        d.click(1765,555)
        d.click(116,966)
        d.press('menu')
        assert d(text="Delete").wait.exists(timeout=5000), 'unable to take picture!'
        d(text='Delete').click.wait()
        d(text="OK").click.wait()

        
            


