# Basic class definition
class Person:
    # Class attribute (shared by all instances)
    species = "Humans"

    # Constructor method to initialize instance attributes
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Method to display person's information
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old." 
    
    # Method with parameter to check if the person is an adult
    def have_birthday(self):
            self.age += 1
            return f"Happy Birthday, {self.name}! You are now {self.age} years old." 

# Creating instances of the Person class  
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

    # Accessing instance attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25

    # Calling instance methods
print(person1.introduce())  # Output: My name is Alice and I am 30 years old.
print(person2.have_birthday())  # Output: Happy Birthday, Bob! You are now 26 years old.

    # Accessing class attribute
print(Person.species)  # Output: Humans
print(person1.species)  # Output: Humans  