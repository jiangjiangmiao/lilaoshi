# Write a program that outputs the top n elements from a list.
#
# Example:
#
# largest(2, [7,6,5,4,3,2,1])
# # => [6,7]


def largest(n, xs):
    """Find the n highest elements in a list"""
    xs.sort(reverse=True)  # 列表降序排序
    return xs[:n]


print(largest(2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(largest(3, [5, 1, 5, 2, 3, 1, 2, 3, 5]))
print(largest(7, [9, 1, 50, 22, 3, 13, 2, 63, 5]))
print(largest(2, [7, 6, 5, 4, 3, 2, 1]))
print(largest(0, [7, 6, 5, 4, 3, 2, 1]))
