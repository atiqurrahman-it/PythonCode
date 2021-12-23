n=int(input("Enter the series "))
a,b=0,1
i=1

while i<=n:
    print(a)
    a=a+b
    a,b=b,a
    i=i+1