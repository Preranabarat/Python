#trafic lite in python using if-elif-else
light=input("light color: ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")



#student grades
marks =int(input("marks: "))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("c")
else:
    print("D")  



# gratetst number 
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
if(a>=b and a>=c):
    print("a is a greatest",a)
elif(b>c and b>=d):
    print("b is a greastest",b)
elif(c>=d):
    print("c is a greastest",c)
else:
    print("d is a greastest",d)



# fee true or flase
A = int(input("A:"))
G = input("M/F:")
if((A==1 or A ==2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G=="F"):
    print("fee is 200")
elif(A==5 and G =="M"):
    print("fee is 300")
else:
    print("no fee")



# single line if-and else / ternary operator
food = input("food:")
eat="yes" if food == "cake" else"no"
print(eat)
food=input("food:")
print("sweet") if food == "cake" or food == "jelabi" else print("no sweet")


# clever if / ternary operator


# voter non voter
age = int(input("age: "))
vote = ("no","yes") [age >= 18]
print(vote)


#tax limit
sal=float(input("salary:"))
tax=sal*(0.1,0.2) [sal >=50000]
print("tax payed",tax)