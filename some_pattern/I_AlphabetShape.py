print("H_AlphabetShape\n")
for row in range(0, 6):
    for col in range(0, 5):
        if col == 2 or row == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
