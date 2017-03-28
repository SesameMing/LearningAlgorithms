#!/usr/bin/env python2
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2017-03-28 16:45


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print fact(6)