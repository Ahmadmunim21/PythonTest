def create_multiplication_table():
    print("🔢 Welcome to the Multiplication Table Generator!")
    
    try:
        # Get the target number from the user
        number = int(input("Enter the number you want a table for: "))
        
        # Get the limit (how many rows to generate)
        limit = int(input("How high should the table go? (e.g., 10 or 12): "))
        
        print(f"\n--- Multiplication Table Generator ---")
        
        # A simple for-loop to do the math and print the results
        for i in range(1, limit + 1):  # 
            result = number * i
            # Using f-strings to format the output nicely
            print(f"{number} x {i} = {result}")
            
        print("----------------------------------\n")
        
    except ValueError:
        # This catches errors if the user types a letter instead of a number
        print("❌ Oops! Please enter valid whole numbers.")

# Run the function
if __name__ == "__main__":
    create_multiplication_table()