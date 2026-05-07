student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science", "History"]
}


# #Assessing values
# print(student["name"])  # Output: John Doe 
# print(student.get("age"))   # Output: 20
# print(student["grade"]) # Output: A
# student["age"] = 21
# #Adding a new key-value pair
# student["email"] = "abc@gmail.com"
# print(student)  # Output: {'name': 'John Doe', 'age': 21, 'grade': 'A', 'courses': ['Math', 'Science', 'History'], 'email': 'abc@gmail.com'}

#Removing a key-value pair
del student['grade']

print(student)  # Output: {'name': 'John Doe', 'age': 21, 'courses': ['Math', 'Science', 'History'], 'email': 'abc@gmail.com'}


keys = student.keys()           #  Get all keys in the dictionary
values = student.values()       #  Get all values in the dictionary
items = student.items()     #  Get all key-value pairs in the dictionary    

print(keys)    # Output: dict_keys(['name', 'age', 'courses', 'email'])
print(values)  # Output: dict_values(['John Doe', 21, ['Math', 'Science', 'History'], 'abc@gmail.com'])
print(items)   # Output: dict_items([('name', 'John Doe'), ('age', 21), ('courses', ['Math', 'Science', 'History']), ('email', 'abc@gmail.com')])


#Iterating through the dictionary
for key in student:
    print(f"{key}: {student[key]}")  # Output: name: John Doe, age: 21, courses: ['Math', 'Science', 'History']
for key, value in student.items():
    print(f"{key}: {value}")  # Output: name: John Doe, age: 21, courses: ['Math', 'Science', 'History'], email:
