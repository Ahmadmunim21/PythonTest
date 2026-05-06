name = input("What is your name? ")
height = float(input("How tall are you? "))

#Input validation

while True:
    try:
        age = int(input("How old are you? "))
        if age > 0 and age < 99:
            break
        else:
            print("Are you that old? Please try again.")
    except ValueError:
        print("Please enter a valid integer for your age.")

#Output Validation

print(f"Hello, {name}! You are {height} tall and {age} years old.")

