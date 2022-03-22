# *           *
# * *         *
# *   *       *
# *     *     *
# *       *   *
# *         * *
# *           *

print("N_AlphabetShape.py")
for row in range(0, 7):
    for col in range(0, 7):
        if col == 0 or col == 6 or col == row:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

