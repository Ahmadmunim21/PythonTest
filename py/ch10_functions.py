# Function with parameters and return value
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Function with return values
def add(a, b):
    return a + b

result = add(5, 3)
print(f"The sum is: {result}")

# Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Bob"))      # Output: Hello, Mr. Bob!
print(greet_with_title("Alice", "Dr.")) # Output: Hello, Dr. Alice!


# # Function with variable-length arguments
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4)) # Output: 10

# # Function with keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

# # Complex *args and **kwargs example
# def complex_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

#     flexible_function(1, 2, 3, name="Alice", age=30)

# Lambda function example (anonymous functions)
square = lambda x: x ** 2
print(square(5))  # Output: 25

add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

# Higher-order function example
def apply_function(func, value):
    return func(value)
result = apply_function(lambda x: x * 2, 5)
print(result)  # Output: 10


