# Enter the any positive number : 5
# Frist way 
#     * 
#   * * 
#   * * * 
#  * * * * 
# * * * * * 
# second way 
#     * 
#   * * 
#   * * * 
#  * * * * 
# * * * * * 



n=int(input("Enter the any positive number : "))

print("Frist way ")
for i in range(1,n+1):
    # sepace print 
    for k in range(0,n-i):
        print(' ',end='')
    # trangle print    
    for j in range(i):
        print("* ",end="")
    print('\n',end='')
    
print("second way ")
for i in range(1,n+1):
    print(" "*(n-i)+ "* "*i)



