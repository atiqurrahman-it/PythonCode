# frist way 
list=[1,20,10,-8,2,4]
ma=max(list)
print("frist way = ",ma)
# frist way second way
def largest_number(lis):
    number=lis[0]
    for i in  lis:
        if number<i:
            number=i
    return number
print("second way = " ,largest_number([1,20,10,-8,2,4]))