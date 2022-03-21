# Enter the any positive number : 5
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 


n=int(input("Enter the any positive number : "))

print("--------Frist  way------------- ")
for i in range(0,n,1):
    #space 
    for s in range(n-i):
        print(" ",end="")
    for p in range(i):
        print("* ",end="")
    print()
for i in range(n,0,-1):
    #space 
    for s in range(n-i):
        print(" ",end="")
    for p in range(i):
        print("* ",end="")
    print()

    
print("--------second way------------- ")

for i in range(0,n,1): # n+n
    print(" "*(n-i)+ "* "*i)
for i in range(n,0,-1):
    print(" "*(n-i)+ "* "*i)

