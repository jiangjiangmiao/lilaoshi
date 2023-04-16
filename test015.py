# Input: 3 and Output:
#   *
#  ***
# *****
#  ###

#  Input 9 and Output:
#     *1
#    ***3
#   *****5
#    ***3
#   *****5
#  *******7
#   *****5
#  *******7
# *********9
#    ###

#  Input 17 and Output:
#       *1
#      ***3
#     *****5
#      ***3
#     *****5
#    *******7
#     *****5
#    *******7
#   *********9
#    *******7
#   *********9
#  ***********11
#   *********9
#  ***********11
# *************13
#      ###

# You can see, always a root, always steps of hight 3, tree never smaller than 3 (return "") and no difference for input values like 15 or 17 (because (int) 15/3 = (int) 17/3).
# That's valid for every input and every tree. Lines are delimited by \r\n and no trailing white space allowed.
# I think there's nothing more to say - perhaps look at the testcases too;-)!

def christmas_tree(height):
    level = int(height / 3)
    for i in range(1, level+1):
        for j in range(1, 4):
            stars = 2 * i + 2 * j - 3
            spaces = level + 3 - i - j
            print(" " * spaces + "*" * stars)
    print(" " * level + "###")


# christmas_tree(17)
# christmas_tree(3)
# christmas_tree(5)
christmas_tree(10)  # *\r\n   ***\r\n  *****\r\n   ***\r\n  *****\r\n *******\r\n  *****\r\n *******\r\n*********\r\n   ###
# christmas_tree(8) # *\r\n  ***\r\n *****\r\n  ***\r\n *****\r\n*******\r\n  ###
# christmas_tree(2)  #
