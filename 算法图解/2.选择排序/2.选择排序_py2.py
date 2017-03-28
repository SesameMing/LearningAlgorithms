#!/usr/bin/env python2
# -*-coding:utf-8-*-
# Author:SesameMing <blog.v-api.cn>
# Email:admin@v-api.cn
# Time:2017-03-28 15:36


def findSmaillest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmaillest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print selectionSort([5, 2, 3, 4, 66, 324, 123])