# Digital root is the recursive sum of all the digits in a number.
#
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
#
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    # ...
    sum = 0
    if n < 0:
        pass
    else:
        n = list(str(n))
        for i in n:
            sum += int(i)
        if sum >= 10:
            return digital_root(sum)
        else:
            return sum


print(digital_root(-16))
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
