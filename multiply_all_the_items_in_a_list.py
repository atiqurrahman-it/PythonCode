# frist way 
list=[1,20,10,-7,2,4]
su=sum(list)
print("frist way = ",su)
# frist way second way
def sum_number(lis):
    ss=0
    for i in  lis:
        ss+=i
    return ss
print("second way = " ,sum_number([1,20,10,-7,2,4]))