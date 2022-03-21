
# Enter the any positive number : 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# Second way !.....
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# -----second part --------
# first way !.....
# *****
#  ****
#   ***
#    **
#     *
# Second way !.....
# *****
#  ****
#   ***
#    **
#     *


n=int(input("Enter the any positive number : "))
# Frist way
for i in range(n,0,-1):
    print("* "*i)
# second way
print("Second way !.....")
for i in range(n,0,-1):
    for j in range(i):
        print("* ",end="")
    print()
    
    
    
print("-----second part --------")
print("first way !.....")
for i in range(n,0,-1):
    # for space print
    for k in range(0,n-i):
        print(' ',end='')
    for j in range(i):
        print("*",end="")
    print()
   
# second way
print("Second way !.....")
for i in range(n,0,-1):
    print(" "*(n-i) + "*"*i)

