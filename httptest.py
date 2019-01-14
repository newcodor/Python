#!/usr/bin/python
# _*_ coding:utf-8 _*_
'''
Author:  newcodor
Time: 2019-1-14
Description:模拟http请求
'''
import socket

def main():
    url="http://www.runoob.com/"
    target=url.split("//")
    if "https:" in target[0]:
        port=443
    elif "http:" in target[0]:
        port=80
    url2=target[1].split("/")
    host=url2[0]
    uri=""
    for x in xrange(1,len(url2)):
        uri+="/"+url2[x]
    # print(uri)
    connect("get",uri,host,80)
    pass

def connect(method,uri,host,port=80):
    sc=socket.socket()
    method=method.upper()
    ip=socket.gethostbyname(host)
    if not sc.connect_ex((ip,port)):
        sc.send(method+" "+uri+" HTTP/1.1\r\nHost: "+host+"\r\nConnection: keep-alive\r\n\r\n")
        print(sc.recv(1024*100000))
        print("send ok！")
    else:
        print("连接失败!")
    sc.close()

if __name__ == '__main__':
    main() 