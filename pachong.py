#!/usr/bin/python2.7
#-*-coding:utf-8-*-

import urllib2, re, string
import threading, Queue, time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
_DATA = []
FILE_LOCK = threading.Lock()
SHARE_Q = Queue.Queue()
_WORKER_THREAD_NUM = 3

class MyThread(threading.Thread):
    def __init__(self,func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()

def worker():
    global SHARE_Q
    while not SHARE_Q.empty():
        url = SHARE_Q.get()
        my_page = get_page(url)
        find_title(my_page)
        time.sleep(1)
        SHARE_Q.task_done()
