# *           *
#   *       *
#     *   *
#       *
# if row == col or (col == 4 and row == 2) or (col == 5 and row == 1) or (col == 6 and row == 0):
print("V_AlphabetShape")
for row in range(0, 4):
    for col in range(0, 7):
        if row == col or (row == 6-col):
            print('* ', end='')
        else:
            print("  ", end="")
    print()
