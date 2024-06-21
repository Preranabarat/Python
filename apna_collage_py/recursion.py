def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
print("end and next line")
show(10)