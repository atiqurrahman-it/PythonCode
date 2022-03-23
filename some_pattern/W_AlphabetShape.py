# *                       *
#   *                   *
#     *       *       *
#       *   *   *   *
#         *       *


print("W_AlphabetShape")
for row in range(0, 5):
    for col in range(0, 13):
        if row == col or row == 12 - col or (row == 3) and (col == 5 or col == 7) or (row == 2 and col == 6):
            print('* ', end='')
        else:
            print("  ", end="")
    print()
