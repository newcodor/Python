#!/usr/bin/python
# _*_ coding:utf-8 _*_
'''
Author:  newcodor
Time: 2019-1-14
Description:模拟http请求
  采用HTTP/1.1协议，使用长连接，添加Connection: keep-alive,
  第一种情况，Reponse响应头中存在Transfer-Encoding: chunked(使用chuck通常是
  服务器端开启了gzip压缩)，这是需要
  根据 \r\n0\r\n 判断数据传输结束，在无法判断响应消息传输长度的情况下使用。
  第二种情况是Content-Length来判断，但这种方式通常浏览器使用的更多；
  这两种方式在HTTP/1.1中只能选其一，但在HTTP/1.0中，使用短连接，有无Content-Length均可，

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
    # ip="127.0.0.1"
    ip=socket.gethostbyname(host)
    if not sc.connect_ex((ip,port)):
        sc.send(method+" "+uri+" HTTP/1.1\r\nHost: "+host+"\r\nConnection: keep-alive\r\n\r\n")
        with open(r"./"+host+".txt","w+") as f:
            buffers=""
            while True:
                data=sc.recv(10240)
                if "\r\n0\r\n" in data:
                    buffers+=data
                    # f.write(data)
                    break
                else:
                    buffers+=data
                    # f.write(data)
                    # print(data)
                pass
            f.write(buffers.split("\r\n\r\n")[1])
            f.close()
        print("send ok！")
    else:
        print("连接失败!")
    sc.close()

if __name__ == '__main__':
    main() 