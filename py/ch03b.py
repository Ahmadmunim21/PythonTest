#Simple Quiz 3 Questions

score = 0
print("Welcome to the quiz! Please answer the following questions:")

# Question 1
answer1 = input("What is the capital of France? ")
if answer1.lower() == "paris":
    score += 1

# Question 2
answer2 = input("What is 5 + 7? ")
if answer2 == "12":
    score += 1

# Question 3
answer3 = input("What is the largest planet in our solar system? ")
if answer3.lower() == "jupiter":
    score += 1
    
print(f"Your final score is: {score}/3")