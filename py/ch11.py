# Basic error handling with try-except

# try:
#         number = int(input("Enter a number: ")) 
#         result = 10 / number
#         print(f"Result: {result}")
# except ValueError:
#         print("Error: Please enter a valid number.")
# except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")

# Using else and finally
# try:
#         number = int(input("Enter a number: ")) 
#         result = 10 / number
# except ValueError:
#         print("Error: Please enter a valid number.")
# except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")
# else:
#         print(f"Result: {result}")
# finally:
#         print("Execution completed.")

# try :
#     file = open("non_existent_file.txt", "r")
# except FileNotFoundError:
#     print("Error: The file does not exist.")
# else:
#     content = file.read()
#     print("File content:")
#     print(content)
# finally:
#     if 'file' in locals():
#         file.close()
#     print("File handling completed.")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("You must be at least 18 years old.")
    return True

try:
    age_input = int(input("Enter your age: "))
    if validate_age(age_input):
        print("Age is valid.")

except ValueError as e:
    print(f"Validation Error: {e}")