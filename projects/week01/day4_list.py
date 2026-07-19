courses = ["History", "Math", "Physics", "CompSci"]

courses_2 = ["Biology", "Turkce"]
print(courses[0])

print(courses[-1]) 

print(courses[0:2])

courses.append("Art")

courses.insert(0, "Education")
print(courses)

courses.extend(courses_2)
print(courses)

courses.remove("Math")

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '555-5555'
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

del student ['age']
print(student.get('name')) 

print(student.get('phone', 'Not Found'))  # This will return 'Not Found' since 'phone' is not a key in the dictionary

print(student)

for key, value in student.items():
    print(key, value)