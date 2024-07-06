list=[]
odd=0
even=0
n=int(input("enter the size of list:"))
for i in range(0,n):
    e=int(input("enter elements:"))
    if e%2==0:
        even=even+1
    else:
        odd=odd+1
    list.append(e)
print("list is ",list)
print("odd are:",odd)
print("even are:",even)

