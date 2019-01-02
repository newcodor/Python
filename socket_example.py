#!/usr/bin/python
# _*_ coding:utf-8 _*_

"""
-------------------------------------------
Date：2019-1-1
Description: 多线程扫描器的开发


-------------------------------------------

"""

import socket as sc
import re
import thread
import time

def main():
    host="47.104.66.96"
    scope=['80','3306','6666','7070','7777']
    for x in scope:
        s=sc.socket()
        s.settimeout(3)
        port=x
        try:
            code = s.connect_ex((host,int(port)))
            s.close()
            if str(code) =="0":
                print(port)
            pass
        except Exception as e:
            s.close()
            raise
            continue
        finally:
            s.close()
            pass

    try:
        thread.start_new_thread(scan,(host,))
        pass
    except Exception as e:
        raise
        print("error:thread start failed")
    else:
        pass
    finally:
        pass
    pass

def  scan(host):
    time.sleep(5)
    scope=['80','3306','6666','7070','7777']
    for x in scope:
        s=sc.socket()
        s.settimeout(3)
        port=x
        try:
            code = s.connect_ex((host,int(port)))
            s.close()
            if str(code) =="0":
                print(port)
            pass
        except Exception as e:
            s.close()
            raise
            continue
        finally:
            s.close()
            pass
            
    #version=re.search("(\d\.)+\d+",response)
    #print(version.group(0))
    #file=open("2.txt","w+")
    #file.write(response)
    #file.close()
    #s.close()
    pass

def  proxy():
    s=sc.socket()
    host="47.104.66.96"
    port=3306
    while(true):
        s.connect((host,port))
        response= s.recv(2*1024)
        pass

    print(response)
    version=re.search("(\d\.)+\d+",response)
    print(version.group())
    file=open("2.txt","w+")
    file.write(response)
    file.close()
    s.close()
    pass  


if __name__ == '__main__':
    main()