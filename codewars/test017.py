# In this kata, you need to write a function that takes a string and a letter as input
# and then returns the index of the nth occurrence of that letter in the string. If there is no such letter in the string,
# then the function should return -1.
# Examples:
#
# second_symbol('Hello world!!!','l', 2) --> 3
# second_symbol('Hello world!!!', 'A', 1) --> -1

def nth_symbol(s, symbol, n):
    if s.count(symbol) == 0:
        return -1
    if s.count(symbol) >= n:
        new_s = list(s)
        for i in range(0, n - 1):
            new_s.remove(symbol)
            i += 1
        first_symbol = new_s.index(symbol)
        return first_symbol + n - 1
    else:
        return -1


print(nth_symbol('Hello world!!!', 'l', 2))
print(nth_symbol('Hello world!!!', 'o', 1))
print(nth_symbol('Hello world!!!', 'A', 1))
print(nth_symbol('', 'q', 1))
print(nth_symbol('Hello Lucy How are you I am fine thank you', 'e', 3))
print(nth_symbol('Hello', 'o', 1))
