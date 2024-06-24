list=[1,2,3,4,5]
pos1=2
pos2=5
temp=list[pos1 -1]
list[pos1-1]=list[pos2-1]
list[pos2-1]=temp

print(list)