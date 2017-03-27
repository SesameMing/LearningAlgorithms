#!/usr/bin/env python

# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2017-03-28 2:13


def binary_search(mylist, item):
    low = 0
    high = len(mylist) - 1
    i = 0
    while low <= high:
        i += 1
        print i
        mid = (low + high)
        guess = mylist[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print binary_search(my_list, 1)
print binary_search(my_list, -1)
