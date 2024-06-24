list=[5,2,3,4,1]
size=len(list)
print("Value of list before changing element")
print(list)
temp=list[0]
list[0]=list[size-1]
list[size-1]=temp
print("Value of list after changing element")
print(list)