#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
#身份证后6位


if __name__ == '__main__':
    sex = '02468' if int(input("性别(男1女2): ")) % 2 == 0 else '13579'  # 性别位
    # sex = '0123456789'  # 性别位
    check = '0123456789X'   # 校验位
    other = '0123456789'   # 其它位
    nums = itertools.product(other, other, sex, check)
    cards = []
    day=31
    for num in nums:
        card_4 ="".join(num)
        for x in range(1,day+1):
            card_6="{}{}".format("0"+str(x) if x<10 else x,card_4)
            cards.append(card_6)
    print("cards size:"+str(len(cards)))
    # print(cards)
    with open("cards.txt","w+",encoding="utf-8") as fo:
        for x in cards:
            fo.write(x+"\n")