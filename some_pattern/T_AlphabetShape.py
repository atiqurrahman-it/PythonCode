# * * * * *
#     *
#     *
#     *
#     *
#     *

print("R_AlphabetShape.py")
for row in range(0, 6):
    for col in range(0, 5):
        if row == 0 or col == 2:
            print('* ', end='')
        else:
            print("  ", end="")
    print()
