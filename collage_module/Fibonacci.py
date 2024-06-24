from functools import reduce

fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1]) if n > 1 else [0] * n

# Example usage:
n = 10
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
