# *           *
#   *       *
#     *   *
#       *
#     *   *
#   *       *
# *           *

print("X_AlphabetShape")
j=6
for row in range(0, 7):
    for col in range(0, 7):
        if row == col or row ==j- col:
            print('* ', end='')
        else:
            print("  ", end="")
    print()
