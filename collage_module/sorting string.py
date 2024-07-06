def custom_sort_string(order, s):
    
    order_index = {char: index for index, char in enumerate(order)}

    sorted_s = sorted(s, key=lambda char: order_index.get(char, len(order)))

    
    return ''.join(sorted_s)

order = "abc"
s = "abcdabc"

sorted_string = custom_sort_string(order, s)
print(sorted_string) 
