# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#  
#
# 示例 1：
#
# 输入：s = "()"
# 输出：true
# 示例 2：
#
# 输入：s = "()[]{}"
# 输出：true
# 示例 3：
#
# 输入：s = "(]"
# 输出：false


def valid(s, m, p):
    i = 0
    for n in s:
        if n == m:
            i += 1
        else:
            if n == p:
                i -= 1
                if i < 0:
                    return False
    return i == 0


def isValid(s):
     return valid(s, "(", ")") and valid(s, "[", "]") and valid(s, "{", "}")

    # i = 0
    # j = 0
    # k = 0
    # for n in s:
    #     if n == "(":
    #         i += 1
    #     else:
    #         if n == ")":
    #             i -= 1
    #             if i < 0:
    #                 return False
    #     if n == "[":
    #         j += 1
    #     else:
    #         if n == "]":
    #             j -= 1
    #             if j < 0:
    #                 return False
    #     if n == "{":
    #         j += 1
    #     else:
    #         if n == "}":
    #             j -= 1
    #             if j < 0:
    #                 return False
    # if i == 0 and j == 0 and k == 0:
    #     return True


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
