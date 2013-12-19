#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d

class MessageTest(unittest.TestCase):
    def setUp(self):
        super(MessageTest, self).setUp()
        d.wakeup()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.press('back')\
         .press('back')\
         .press('home')

    def tearDown(self):
        d.press('back')\
         .press('back')\
         .press('back')\
         .press('home')

    def testSendMessage1(self):
        assert d.exists(text='Messaging') , 'message app not appear on the home screen'
        #assert d.exists(text='Apps')  , 'apps not appear on the home screen'
        d(text='Messaging').click.wait()
        if not d(text="No messages").wait.exists(timeout=3000):
            d.press('menu')
            d(text="Delete threads").click.wait()
            d(text="Select all").click.wait()
            d(text="Delete").click.wait()
            d(text="OK").click.wait()
            assert d(text="No messages").wait.exists(timeout=10000)
        d(description='Compose').click.wait()
        d(text='Enter recipient').set_text('13581739891')
        assert d(text="13581739891").wait.exists(timeout=10000), 'receiver number input error'            
        d(text='Enter message').set_text('testingongoing')
        assert d(text="Testingongoing").wait.exists(timeout=10000), 'content input error'            
        d(description='Send').click.wait()
        assert d(className='android.widget.ProgressBar').wait.gone(timeout=10000), 'message unable to send in 30 seconds'
        assert d(description='Sending failed').wait.exists(timeout=10000), 'message send failed'
        assert d(text='Failed').wait.exists(timeout=10000), 'message send failed'




            

