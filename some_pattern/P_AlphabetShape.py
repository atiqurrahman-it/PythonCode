# * * * * *
# *         *
# *         *
# * * * * *
# *
# *
# *

print("P_AlphabetShape.py")
for row in range(0, 7):
    for col in range(0, 6):
        if (col == 0) or (row == 0 or row == 3) and (col > 0 and col < 5) or (col == 5) and (row > 0 and row < 3):
            print("* ", end="")
        else:
            print("  ", end="")
    print()
