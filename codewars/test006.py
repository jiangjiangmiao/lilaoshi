# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]


def unique_in_order(sequence):
    sequence = list(sequence)
    res = []
    last = None
    for i in sequence:
        if last == i:
            continue
        res.append(i)
        last = i
    return res


print(unique_in_order(""))
print(unique_in_order([]))
print(unique_in_order(()))

print(unique_in_order("A"))
print(unique_in_order(["A"]))
print(unique_in_order(("A",)))

print(unique_in_order("AA"))
print(unique_in_order("AAAABBBCCDAABBB"))

print(unique_in_order("ABBCcA"))

print(unique_in_order([1, 2, 3, 3, -1]))
print(unique_in_order(["a", "b", "b", "a"]))
