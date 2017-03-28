#!/usr/bin/env python2
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2017-03-28 17:16


def sum(arr):
    if len(arr) > 0:
        return arr.pop() + sum(arr)
    elif len(arr) == 0:
        return 0
    else:
        return arr[0]


print sum([1, 2, 3, 100, 100000])