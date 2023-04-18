# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
#
# Don't forget the space after the closing parentheses!

def create_phone_number(n):
    # your code here
    if len(n) <= 10:
        # return "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + str(n[3]) + str(n[4]) + str(n[5]) + "-" + str(
        #     n[6]) + str(n[7]) + str(n[8]) + str(n[9])

        list1 = [str(i) for i in n[0:3]]
        list2 = [str(i) for i in n[3:6]]
        list3 = [str(i) for i in n[6:]]
        return "(" + str(''.join(list1)) + ") " + str(''.join(list2)) + "-" + str(''.join(list3))
    else:
        return False


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
