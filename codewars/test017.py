# In this kata, you need to write a function that takes a string and a letter as input
# and then returns the index of the nth occurrence of that letter in the string. If there is no such letter in the string,
# then the function should return -1. If the letter occurs only once in the string, then -1 should also be returned.
#
# Examples:
#
# second_symbol('Hello world!!!','l', 2) --> 3
# second_symbol('Hello world!!!', 'A', 1) --> -1

def nth_symbol(s, symbol, n):
    pass


print(nth_symbol('Hello world!!!', 'l', 2))
print(nth_symbol('Hello world!!!', 'o', 1))
print(nth_symbol('Hello world!!!', 'A', 1))
print(nth_symbol('', 'q', 1))
print(nth_symbol('Hello Lucy How are you I am fine thank you', 'e', 3))
