class student:
    #defulkt constructors
    # def __init__(self):
    #     pass
    #parametarize constructors
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in database")

s1=student("prerana")
s2=student("mewmew")
print(s1.name)
print(s2.name)