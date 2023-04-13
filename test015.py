# Input: 3 and Output:
#   *
#  ***
# *****
#  ###

#  Input 9 and Output:
#     *
#    ***
#   *****
#    ***
#   *****
#  *******
#   *****
#  *******
# *********
#    ###

#  Input 17 and Output:
#       *
#      ***
#     *****
#      ***
#     *****
#    *******
#     *****
#    *******
#   *********
#    *******
#   *********
#  ***********
#   *********
#  ***********
# *************
#      ###

# You can see, always a root, always steps of hight 3, tree never smaller than 3 (return "") and no difference for input values like 15 or 17 (because (int) 15/3 = (int) 17/3).
# That's valid for every input and every tree. Lines are delimited by \r\n and no trailing white space allowed.
# I think there's nothing more to say - perhaps look at the testcases too;-)!

def christmas_tree(height):
    # Coding a nice christmas tree ^_^
    pass


print(christmas_tree(5))  # *\r\n ***\r\n*****\r\n ###
print(christmas_tree(10))  # *\r\n   ***\r\n  *****\r\n   ***\r\n  *****\r\n *******\r\n  *****\r\n *******\r\n*********\r\n   ###
print(christmas_tree(8))  # *\r\n  ***\r\n *****\r\n  ***\r\n *****\r\n*******\r\n  ###
print(christmas_tree(2))  #
