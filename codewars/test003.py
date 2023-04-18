# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= length of input <= 100
#
# All inputs will be strings, consisting only of characters ( and ).
# Empty strings are considered balanced (and therefore valid), and will be tested.
# For languages with mutable strings, the inputs should not be mutated.


def valid_parentheses(paren_str):
    i = 0
    for n in paren_str:
        if n == "(":
            i += 1
        else:
            i -= 1
            if i < 0:
                return False
    return i == 0


print(valid_parentheses("()"))
print(valid_parentheses("((()))"))
print(valid_parentheses("()()()"))
print(valid_parentheses("(()())()"))
print(valid_parentheses("()(())((()))(())()"))

print(valid_parentheses(")("))
print(valid_parentheses("()()("))
print(valid_parentheses("((())"))
print(valid_parentheses("())(()"))
print(valid_parentheses(")()"))
print(valid_parentheses(")"))

print(valid_parentheses(""))
