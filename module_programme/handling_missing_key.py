def missingkey(duic,keys):
    for key,value in duic.items():
        if key == keys:
            return True
        else:
            return False

dict = {1:"mew mew",2:"Prerana"}
iskey = missingkey(dict,3)
if iskey:
    print("key is persent")
else:
    print("key is not present")