n=int(input(" How many terms?"))
a,b=0,1
i=1
if n <= 0:
   print("Please enter a positive integer")
else:
    while i<=n:
        print(a)
        a=a+b
        a,b=b,a
        i=i+1