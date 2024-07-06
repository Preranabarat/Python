def common_element(l1,l2):
    set1=set(l1)
    set2=set(l2)
    if set1 & set2:
        return True
    else:
        return False

list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
i=common_element(list1,list2)
if i==True:
    print("The list have atlist one element common element")

else:
    print("The list do not have any common element")