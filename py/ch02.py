# String Manipulation
greeting = "Hello, World!"
print(greeting) # Output: Hello, World!
# String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name) # Output: John Doe
# String Repetition
echo = "Echo! " * 3
print(echo) # Output: Echo! Echo! Echo!
# String Slicing
message = "Python Programming"
print(message[0:6]) # Output: Python
print(message[7:18]) # Output: Programming
# String Methods
text = "   Hello, World!   "
print(text.strip()) # Output: Hello, World!
print(text.lower()) # Output:    hello, world!
print(text.upper()) # Output:    HELLO, WORLD!
print(text.replace("World", "Python")) # Output:    Hello, Python! 

# String Formatting
name = "Alice"
age = 30

# Using f-strings
print(f"My name is {name} and I am {age} years old.") # Output: My name is Alice and I am 30 years old.
# Using str.format()
print("My name is {} and I am {} years old.".format(name, age)) # Output: My name is Alice and I am 30 years old.
# Using % operator
print("My name is %s and I am %d years old." % (name, age)) # Output: My name is Alice and I am 30 years old.


single_quote = 'It\'s a nice day!' # Using escape character
double_quote = "She said, \"Hello!\"" # Using escape character
triple_quote = """This is a multi-line string. It can span multiple lines without needing escape characters.""" # Using triple quotes for multi-line string


print(single_quote) # Output: It's a nice day!
print(double_quote) # Output: She said, "Hello!"    \# Raw String
print(triple_quote) # Output: This is a multi-line string. It can span multiple lines without needing escape characters.   

raw_string = r"C:\Users\Alice\Documents"
print(raw_string) # Output: C:\Users\Alice\Documents