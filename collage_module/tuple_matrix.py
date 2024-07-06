def row_addition(matrix):
    result = []
    for row in matrix:
        row_sum = sum(row)
        result.append(row_sum)
    return tuple(result)
    
tuple_matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Original Tuple Matrix:")
for i in tuple_matrix:
    print(i)
print("\nRow-wise Element Addition:")
print(row_addition(tuple_matrix))