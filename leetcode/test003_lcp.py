# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
#  
#
# 示例 1：
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。

def lcp(array):
    len_min = min(array, key=len)
    y = ''
    for j in range(0, len(len_min)):
        x = ''
        for i in range(0, len(array)):
            if i == 0:
                x = array[0][j]
            elif array[i][j] == x:
                continue
            else:
                return y
        y += array[0][j]
    return y


# def lcp(array):
#     len_min = min(array, key=len)
#     for i in range(0, len(len_min)):
#         for n in array:
#             if


print(lcp(["flower", "flow", "flight"]))
print(lcp(["dog", "racecar", "car"]))
