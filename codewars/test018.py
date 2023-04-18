# You'll have to return a string that contains dots, as many the equation returns. If the result is 0, return the empty string. When it comes to subtraction,
# the first number will always be greater than or equal to the second number.
#
# Examples (Input => Output)
# * "..... + ..............." => "...................."
# * "..... - ..."             => ".."
# * "..... - ."               => "...."
# * "..... * ..."             => "..............."
# * "..... * .."              => ".........."
# * "..... // .."             => ".."
# * "..... // ."              => "....."
# * ". // .."                 => ""
# * ".. - .."                 => ""


def calc(txt):
    # This is the place to code!

    space = txt.index(" ")
    symbol = txt[space + 1]
    left = txt[:space]
    right = txt[space + 3:]
    if left.count('.') < right.count('.') and symbol == '-' or left.count('.') < right.count('.') and symbol == '/':
        return "' '"
    if symbol == "+":
        return (left.count('.') + right.count('.')) * "."
    if symbol == "-":
        return (left.count('.') - right.count('.')) * "."
    if symbol == "*":
        return (left.count('.') * right.count('.')) * "."
    if symbol == "/":
        return (left.count('.') // right.count('.')) * "."


# print(calc("..... + ..............."))
# print(calc("..... - ..."))
# print(calc("..... - ."))
# print(calc("..... * ..."))
print(calc(". // .."))
print(calc("..... // ."))
print(calc("..... + ..............."))
