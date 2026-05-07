# Nested dictionaries
# A nested dictionary is a dictionary that contains another dictionary as a value.
company = {
    "employees": { 
        "employee1": {"name": "Alice", "age": 30, "department": "HR"},
        "employee2": {"name": "Bob", "age": 25, "department": "IT"},
        "employee3": {"name": "Charlie", "age": 35, "department": "Finance"}
    },
    "locations": ["New York", "Los Angeles", "Chicago"]
}

print(company["employees"].items()) # Output: dict_items([('employee1', {'name': 'Alice', 'age': 30, 'department': 'HR'}), ('employee2', {'name': 'Bob', 'age': 25, 'department': 'IT'}), ('employee3', {'name': 'Charlie', 'age': 35, 'department': 'Finance'})])
print(company["locations"][1])  # Output: Los Angeles
