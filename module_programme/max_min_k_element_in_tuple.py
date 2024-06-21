
main_list = []
size = int(input("Enter the list size: "))

for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    main_list.append(element)

print("List is:", main_list)
sorted_list = sorted(main_list)
print("The sorted list is:", sorted_list)

k = int(input("Enter the value of k: "))

maximum_k = sorted_list[-k:]
minimum_k = sorted_list[:k]

print("Maximum k elements are:",maximum_k)
print("Minimum k elements are:",minimum_k)