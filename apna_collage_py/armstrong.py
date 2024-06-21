n=int(input("enter the integer number:"))
temp=n
sum=0


while(n>0):
    r=int(n%10)
    sum=sum+(r*r*r)
    n=int(n/10)

if temp==sum:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")
