p=int(input("enter the principle amount:"))
t=int(input("enter the time period:"))
r=int(input("enter interest rate:"))
a=p*(pow((1+r/100),t))
ci=a-p
print("the compound interast is :",ci)