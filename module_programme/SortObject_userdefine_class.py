class mewmew:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def bubble_sort(obj):
    size = len(obj)
    for i in range(size):
        for j in range(0,size-i-1):
            if obj[j].age > obj[j+1].age:
                obj[j],obj[j+1] = obj[j+1],obj[j]

obj = []
while True:
    name = input("Enter your name(if you want to finish enter done)")
   
    if name.lower() == 'done':
     break
    age = input("Enter your age")
    obj.append(mewmew(name,age))

bubble_sort(obj)
for i in obj:
    print(f'{i.name} {i.age}')