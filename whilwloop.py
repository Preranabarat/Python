# num=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(num):
#     print(num[idx])
#     idx+=1
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at index", i)
    i += 1
