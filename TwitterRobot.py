#!/usr/bin/env Python
# _*_ coding:utf-8 _*_
#Author: Shawn

'''
这个玩具代码的twitter API框架主要来自于Github的开源项目：“TwitterAPI”。由于这个玩具代码的大部分功能都依赖于这个项目，在此表示感谢。
使用TwitterRobort之前，需要在twitter开发者网页上申请 consumer_key,consumer_secret,access_token_key,以及access_token_secret。申请完毕之后，需要将这些验证信息填入代码的‘—————’处
'''

import codecs
from datetime import datetime
import sys
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRestPager
import time
import datetime

try:
    # python 3
    sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
except:
    # python 2
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)

consumer_key='____'         #申请的验证信息，填在这里
consumer_secret='____'
access_token_key='____'
access_token_secret='____'

api=TwitterAPI(consumer_key,consumer_secret,access_token_key,access_token_secret)

n=1
while n==1:        #  无限死循环
    current_time=datetime.datetime.now() #获得当前时间
    times=current_time.hour   #获取当前HOUR（24小时制）
    print_chr=times*' duang'   #打印DUANG的次数，可以修改打印的字符
    time_now=time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))   #获得当前准确时间

    r=api.request('statuses/update',{'status':time_now}) 
    r=api.request('statuses/update',{'status':print_chr}) 
    print r.status_code

    time.sleep(3600)  #暂停1小时候，再次启动循环

#发送TWITTER及其消息内容，限制140字：

