# Create a function named rotate() that accepts a string argument and returns an array of strings with each letter from the input string being rotated to the end.
#
# rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"]
# Note: The original string should be included in the output array The order matters.
# Each element of the output array should be the rotated version of the previous element.
# The output array SHOULD be the same length as the input string The function should return an emptry array with a 0 length string, '', as input


def rotate(string):
    new_list = []
    if len(string) == 0:
        return []
    else:
        for i in range(1, len(string)):
            new_str = string[i:] + string[:i]
            new_list.append(new_str)
        new_list.append(string)
        return new_list


print(rotate("Hello"))  # ["elloH", "lloHe", "loHel", "oHell", "Hello"]
print(rotate(" "))  # [" "]
print(rotate(""))  # []
print(rotate("123"))  # ["231", "312", "123"]
