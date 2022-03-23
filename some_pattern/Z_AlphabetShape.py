# * * * * * * *
#           *
#         *
#       *
#     *
#   *
# * * * * * * *

print("Z_AlphabetShape")
j=6
for row in range(0, 7):
    for col in range(0, 7):
        if (row==0 or row==6) or row ==j- col:
            print('* ', end='')
        else:
            print("  ", end="")
    print()
