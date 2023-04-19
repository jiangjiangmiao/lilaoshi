# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.


def find_uniq(arr):
    # your code here
    # 这道题要注意性能
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]


print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))
print(find_uniq([3, 10, 3, 3, 3]))
