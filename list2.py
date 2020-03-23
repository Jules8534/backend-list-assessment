#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie assignment: List2
"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Instructions:
# Complete each of these list manipulation exercises in the same way as the 
# previous List1 excercises.

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
# Hint: Don't use `set()`


def remove_adjacent(nums):
    res = []
    for el in nums:
        if res:
            if res[-1] != el:
                res.append(el)
        else:
                res.append(el)

    # while i < len(nums):
    #     if nums[i] == nums [i-1]:
    #        nums.pop(i)
    #     i += 1 
    return res


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# The solution should work in "linear" time, making a single pass of both lists.
# Hint: Don't use `sort` or `sorted` -- they are not O(n) linear time, and the two lists
# are already provided in ascending sorted order.
def linear_merge(list1, list2):
    res = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            el = list1[0]
            list1 = list1[1:]
        else:
            el = list2[0]
            list2 = list2[2:]
        res.append(el)
    while len(list1):
        res.append(list1[0])
        list1 = list1[1:]
    while len(list2):
        res.append(list2[0])
        list2 = list2[1:]
    return res

    #     result.append((list1 if list1[-1] > list2[-1] else list2).pop(-1))
    # result += list1 if len(list1) else list2
    # return result[-1::-1]


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    test(remove_adjacent([2, 2, 3, 3, 3, 4, 5, 2, 3]), [2, 3, 4, 5, 2, 3])

    print('')
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
