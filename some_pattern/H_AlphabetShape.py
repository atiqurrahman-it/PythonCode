print("H_AlphabetShape\n")
for row in range(0, 7):
    for col in range(0, 5):
        if col == 0 or col == 4 or row==3:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
