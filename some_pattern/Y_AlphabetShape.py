# *           *
#   *       *
#     *   *
#       *
#       *
#       *


print("Y_AlphabetShape")
j = 6
for row in range(0, 7):
    for col in range(0, 7):
        if ((row == col) and (row >= 0 and row < 3)) or ((row == j - col)and (row >= 0 and row < 3)) or col==3 and(row>2 and row<6):
            print('* ', end='')
        else:
            print("  ", end="")
    print()
