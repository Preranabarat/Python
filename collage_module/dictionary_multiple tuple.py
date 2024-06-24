num=int(input("enter number of students:"))
student={}
for i in range(num):
    roll=i+1
    name=input("enter name:")
    marks=int(input("enter marks:"))
    student[roll]=[[name],[marks]]
print(student)