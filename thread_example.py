#!/usr/bin/python
#  _*_  coding=utf-8 _*_

"""
----------------------------

Date: 2019-1-2
Description: 多线程实例

----------------------------

"""

import threading 
import time


sum = 0

def   sums(n):
    global sum
    sum = sum + n
    time.sleep(1)
    sum = sum - n
    print "threading %s running %d......" % (threading.current_thread().name,sum)

def  exp(n):
    for x in xrange(0,100):
        sums(n)



def main():
    # exp("11")
    t1=threading.Thread(target=exp,args=(5,))
    t2=threading.Thread(target=exp,args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("sum:"+str(sum))

if __name__ == '__main__':
    main()

