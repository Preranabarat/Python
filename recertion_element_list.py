def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["mango","orange","lichi","apple","banana","graps","avogrado"]

print_list(fruits)