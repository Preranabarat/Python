def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different numbers of keyword arguments
print_kwargs(name="Alice", age=23, city="New York")
print_kwargs(a=1, b=2, c=3)
