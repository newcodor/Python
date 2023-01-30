#!/usr/bin/env python
# -*- coding:utf-8 -*

#cidr calculator

import copy

def getIpListFromStr(ipStr):
    return [int(ipStr[i:i+8],2) for  i in range(0,len(ipStr),8)]


def getNetId(cidrIp,netIdLength=None):
    cidr_item=cidrIp.split("/")
    ip=cidr_item[0]
    if not netIdLength:
        netIdLength=int(cidr_item[1])
    binStr=""
    for block in ip.split("."):
        # print(block,"{:08b}".format(int(block)))
        binStr+="{:08b}".format(int(block))
    netId=binStr[:netIdLength]
    return netId,netIdLength

def cidrToScope(cidr):
    if "/" in cidr:
        mask=[255,255,255,255]
        netId,netIdLength = getNetId(cidr)
        print("getNetId:",netId)
        network = getIpListFromStr(netId+"0"*(32-netIdLength))
        broadcastAddr = getIpListFromStr(netId+"1"*(32-netIdLength))
        firstAddr = copy.copy(network)
        firstAddr[-1] = firstAddr[-1]+1
        endAddr =copy.copy(broadcastAddr)
        endAddr[-1] = endAddr[-1]-1
        # print(network)
        # print(broadcastAddr)
        # print(firstAddr)
        # print(endAddr)

        #get mask
        pos=int(netIdLength/8)
        varNum = 256-2**(8*(int(netIdLength/8)+1)-netIdLength)
        mask[pos] = varNum
        for i in range(pos+1,len(mask)):
            mask[i]=0
        # print(mask)
        return mask,network,broadcastAddr,firstAddr,endAddr
    pass

# check ip is in cidr
def containIp(cidr,ip):
    cidrNetId,netIdLength = getNetId(cidr)
    ipNetId,_ = getNetId(ip,netIdLength)
    if cidrNetId == ipNetId:
        return True
    return False

def main():
    print(cidrToScope("10.110.101.11/13"))
    print(containIp("10.110.101.11/13","10.104.0.0"))
    pass

if __name__ == '__main__':
    main()