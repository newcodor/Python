#!/usr/bin/python
# _*_ coding:utf-8 _*_

"""
-------------------------------------------
Date：2019-1-1
Description: 基于同步锁实现线程安全的多线程扫描器的研究
Case:
    port scope:5000-10000
    speed time:154.9s

-------------------------------------------

"""

import socket as sc
import re
import threading
import time




def main():
    threadpool=[]
    global host
    global max_port
    for x in xrange(1,100):
        th=threading.Thread(target=scan,args=(host,max_port))
        threadpool.append(th)
        th.start()
        pass
    for x in threadpool:
        x.join()

    print("\n------------------------------")
    open_port.sort()
    if len(open_port)>0:
        print("open ports count: "+str(len(open_port)))
        for x in open_port:
            print(x)
            pass
    else:
        print("no open port!")
    print("------------------------------")


    
def  scan(host,max_port):
    global current_port
    global threadLock
    while True:
        s=sc.socket()
        s.settimeout(3)
        try:
            if threadLock.acquire():
                if  current_port >= max_port:
                    threadLock.release()
                    break
                port=current_port
                current_port=current_port+1
                threadLock.release()
            code = s.connect_ex((host,port))
            s.close()
            if str(code) =="0":
                print(str(port)+" is open\n")
                open_port.append(port)
            else:
                # print(str(port)+" is close\n")
                pass
            pass
        except Exception as e:
            s.close()
            raise
        finally:
            s.close()
            pass
            

if __name__ == '__main__':
    open_port=[]
    current_port=5000
    max_port=10000
    host="47.104.66.96"
    threadLock = threading.Lock()
    main()