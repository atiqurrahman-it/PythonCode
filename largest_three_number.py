a,b,c=111,1055,88

if(a<b):
    if(b<c):
        print(c)
    else:
        print(b)
elif(a<c):
    print(c)
else:
    print(a)
    
# type 2     
learge=(a if (a>b and a>c) else (b if (b>a and b>a) else c))
print(learge)

# type 3 
if (a>b) and (a>c):
    print(a)
elif (b>a) and (b>c):
    print(b)
else:
    print(c)
    
# type 4
def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

print(maximum(a,b,c))
    

    