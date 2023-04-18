# Given an array of numbers, return the difference between the largest and smallest values.
# For example:
# [23, 3, 19, 21, 16] should return 20 (i.e., 23 - 3).
# [1, 434, 555, 34, 112] should return 554 (i.e., 555 - 1).
# 写一个函数计算数字里最大的数和最小的数的差
#
# def between_extremes(numbers):
#     #Your code goes here!
#     pass
# 测试用例：
# test.assert_equals(between_extremes([1, 1]), 0, 'Expecting zero when all numbers are equal')
# test.assert_equals(between_extremes([-1, -1]), 0, 'Expecting zero when all numbers are equal')
# test.assert_equals(between_extremes([1, -1]), 2)
# test.assert_equals(between_extremes([21, 34, 54, 43, 26, 12]), 42)
# test.assert_equals(between_extremes([-1, -41, -77, -100]), 99)

import sys


def between_extremes(numbers):
    # Your code goes here!
    max_num = -sys.maxsize
    min_num = sys.maxsize
    for i in numbers:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    return max_num - min_num


print(between_extremes([1, 1]))
print(between_extremes([-1, -1]))
print(between_extremes([1, -1]))
print(between_extremes([21, 34, 54, 43, 26, 12]))
print(between_extremes([-1, -41, -77, -100]))
