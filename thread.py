#!/usr/bin/python2.7
#-*-coding:utf-8-*-
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        super(MyThread, self).__init__()
        self.thread_id = thread_id
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting:" + self.name
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()
def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s %s" %(thread_name, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

thread1 = MyThread(1, "thread-1", 1)
thread2 = MyThread(2, "thread-2", 2)

thread1.start()
thread2.start()

for t in threads:
    t.join()
print "exiting main thread"
