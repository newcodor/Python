#!/usr/bin/python
# _*_ coding:utf-8 _*_

"""
-------------------------------------------
Date：2019-1-1
Description: 多线程扫描器的开发
Case:
    port scope:5000-10000
    speed time:154.0s

-------------------------------------------

"""

import socket as sc
import threading
import time
import Queue



def main():
    host="47.104.66.96"
    threadpool=[]
    max_port=10000
    for i in range(5000,max_port):
        q.put(int(i))
    for x in xrange(1,100):
        th=threading.Thread(target=scan,args=(host,max_port))
        threadpool.append(th)
        th.start()
        pass
    for x in threadpool:
        x.join()

    print("\n------------------------------")
    open_ports=list(set(open_port))
    if len(open_ports)>0:
        print("open ports count: "+str(len(open_ports)))
        for x in open_ports:
            print(x)
            pass
    else:
        print("no open port!")
    print("------------------------------")


    
def  scan(host,max_port):
    while True:
        s=sc.socket()
        s.settimeout(5)
        try:
            if  q.empty():
                break
            port=q.get()
            code = s.connect_ex((host,port))
            q.task_done()
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
    q = Queue.Queue()
    open_port=[]
    main()