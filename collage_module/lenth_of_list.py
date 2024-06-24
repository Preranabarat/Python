list=[1,2,3,4,5,6,7,8,9]
#way one
length1=len(list)

print("Length of the list: ")
print(length1)

#way 2
sum1=0
for i in list:
    sum1+=1
print("Length of the list: ")
print(sum1)


#way 3
length2=sum([1 for _ in list])
print("Length of the list: ")
print(length2)