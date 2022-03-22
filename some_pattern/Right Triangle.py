# Enter the any positive number : 5
# Right trangle part 1
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# Second way !.....
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# Right trangle part 2
# * 
# * * * 
# * * * * * 
# Second way !.....
# * 
# * * * 
# * * * * * 

n = int(input("Enter the any positive number : "))
print("Right trangle part 1")

# first way
for i in range(1, n + 1):
    for j in range(i):
        print("* ", end="")
    print()
# second way
print("Second way !.....")
for i in range(1, n + 1):
    print("* " * i)

print("Right trangle part 2")
# second way
for i in range(1, n + 1):
    if i % 2 != 0:
        print("* " * i)
# second way
print("Second way !.....")
for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(i):
            print("* ", end="")

        print()
