#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time,subprocess

def get_strftime():
    now = int(time.time())
    timeStruct = time.localtime(now)
    current_time=time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
    # current_time=time.strftime("%Y-%m-%d 14:%M:%S", timeStruct)
    return current_time


def click(x,y):
    subprocess.check_output(f"adb shell input tap {x} {y}")


def send_click(x,y):
    # not permision for no root privilege!
    subprocess.check_output("adb shell sendevent /dev/input/event7 3 57 45447")
    subprocess.check_output(f"adb shell sendevent /dev/input/event7 3 53 {x*10}")
    subprocess.check_output(f"adb shell sendevent /dev/input/event7 3 54 {y*10}")
    subprocess.check_output("adb shell sendevent /dev/input/event7 1 330 1")
    subprocess.check_output("adb shell sendevent /dev/input/event7 1 325 1")
    subprocess.check_output("adb shell sendevent /dev/input/event7 0 0 0")
    subprocess.check_output("adb shell sendevent /dev/input/event7 3 57 -1")
    subprocess.check_output("adb shell sendevent /dev/input/event7 1 330 0")
    subprocess.check_output("adb shell sendevent /dev/input/event7 1 325 0")
    subprocess.check_output("adb shell sendevent /dev/input/event7 0 0 0")



def meituan(x,y):
    today_date=get_strftime().split(" ")[0]
    trigger_time=f"{today_date} 10:00:00"
    print("trigger_time:",trigger_time)
    print("start monitor ....")
    while True:
        current_time = get_strftime()
        if current_time == trigger_time:
            time.sleep(0.05)
            for i in range(0,15):
                click(x,y)
                time.sleep(0.1)
            print("\n")
            print(get_strftime())
            break
        # print(".",end="")
    pass

def action_chain(action_group):
    print("[+] start ....")
    start_time = time.time()
    for act in action_group:
        click(act[0],act[1])
        time.sleep(act[2])
    print(time.time()-start_time)


def test_jd(location):
    for i in range(0,9):
        click(location[0],location[1])
        time.sleep(0.1)

if __name__ == "__main__":
    # china_12306_action_group=[(824.1,1452.4,0.7),(265.6,987.6,0.5),(776,589.7,0),(990.3,147.7,0.5),(854.6,1473.9,0.4),(448,1898,0)]
    # china_12306_action_group=[(824.1,1452.4,0.7),(265.6,987.6,0.5),(776,589.7,0),(990.3,147.7,0.5),(854.6,1473.9,0.4)]
    # action_chain(china_12306_action_group)
    # 周一、二:26-18
    meituan(860.7,1143.8)
    # 每月18： 38-18
    # meituan(851.6,1373.6)
    # test_jd((987.7,733.4))
    # click(860.7,1143.8)