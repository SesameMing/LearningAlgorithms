#!/usr/bin/env python3
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2016-11-28 14:08


def main():
    li = []
    for i in range(100):
        li.append(0)

    num = input("准备输入几个数字:").strip()
    for y in range(int(num)):
        t = input("数字:")
        li[int(t)] += 1

    for s in range(100):
        if li[int(s)] >= 1:
            for z in range(li[int(s)]):
                print(s, end=' ')

if __name__ == '__main__':
    main()