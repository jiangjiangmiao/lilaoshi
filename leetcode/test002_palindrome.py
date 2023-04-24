# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
#
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 例如，121 是回文，而 123 不是。
#
#
# 示例 1：
#
# 输入：x = 121
# 输出：true
# 示例 2：
#
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3：
#
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。
#
#
# 提示：
#
# -231 <= x <= 231 - 1
#
#

def isPalindrome(x):
    a = list(str(x))
    b = [x for x in a]
    a.reverse()
    return a == b


def isPalindrome2(x):
    x = str(x)
    y = x[::-1]
    return x == y


def isPalindrome3(n):
    if n < 0:
        return False
    x = []
    while n > 0:
        i = n % 10
        x.append(i)
        n = n // 10
    y = x[::-1]
    return x == y


print(isPalindrome3(121))
print(isPalindrome3(-121))
print(isPalindrome3(1234))
