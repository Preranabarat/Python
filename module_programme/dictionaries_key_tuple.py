#key
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
sorted_d = dict(sorted(d.items()))

print(sorted_d)

#value

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))

print(sorted_d)