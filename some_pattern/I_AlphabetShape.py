print("I_AlphabetShape\n")
for row in range(0, 6):
    for col in range(0, 3):
        if col == 1 or row == 0 or row==5:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
