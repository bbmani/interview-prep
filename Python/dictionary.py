from collections import Counter
student = {'name': 'John', 'courses': ['Math', 'CompSci']}

print(student.get('name'))
print(student.get('Phone', 'Not Found'))

# NEW ENTRY TO DICTIONARY
student.update({'name': 'john', 'age':26, 'phone':"555-555-5555"})

# PRINTING THE STUDENT DICTIONARY
for key, value in student.items():
    print(f"Key : {key}, Value : {value}")

# sorting the array based on frequency, but if two numbers have the same frequency reverse them only

numbers = [2,3,1,3,2]
res = []
first_sort = dict(sorted(Counter(numbers).items(), reverse=True))
print(first_sort)
second_sort = dict(sorted(first_sort.items(), key=lambda x:x[1]))
print(second_sort)
for key, value in second_sort.items():
    res.extend([key] * value)
print(res)