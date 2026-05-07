grades = [  ("Alice", "Math", 85),  ("Bob", "Science", 92),  ("Alice", "Science", 78),  ("Charlie", "Math", 90),  ("Bob", "Math", 88),  ("Alice", "English", 95) ]


# Have to create empty sets to store the unique data
name = set()
subject = set()

# Have to loop each tuple in grades list

for record in grades:
    name.add(record[0])
    subject.add(record[1])

print("Unique Students:", name)
print("Unique Subjects:", subject)