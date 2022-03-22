# * * * * * *
# *
# *
# * * * * * *
# *
# *
# *

print("F_AlphabetShape\n")
for row in range(7):
    for col in range(6):
        if (col == 0) or (row == 0 or row == 3):
            print("* ", end="")
        else:
            print("  ", end="")
    print()
