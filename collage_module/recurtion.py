def power(n,p):
    #base case
    if(p==0):
        return 1
    #recursive case
    ans=n*power(n,p-1)
    return ans

n=int(input("enter the number "))
p=int(input("enter the power "))
p=power(n,p)
print(p)