
#   * * * *
# *
# *
# *     * * *
# *       *
# *       *
#   * * *


print("G_AlphabetShape\n")
for row in range(0, 7):
    for col in range(0, 6):
        if ((col == 0) and (row != 0 and row != 6)) or ((col == 4) and (row != 1 and row != 2 and row != 6)) or (
                (row == 0 or row == 6) and (col > 0 and col < 4)) or ((row == 3) and (col == 3 or col == 5)):
            print("* ", end="")
        else:
            print("  ", end="")
    print()

# ((col == 0) and (row != 0 and row != 6)) first col er

# ((col == 4) and (row != 1 and row != 2 and row != 6)) for col er

# (row == 0 or row == 6) and (col > 0 and col < 4)) row 1 and 6 er
# ((row == 3) and (col == 3 or col == 5)) row 3 er
