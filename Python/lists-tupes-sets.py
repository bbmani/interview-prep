courses = ["History", "Math", "Physics", "CompSci"]
print(f"Printing the total Length of courses : {len(courses)}")
print(f"The courses list : {courses}")
print(f"Two ways to print the last element: {courses[len(courses) - 1]} {courses[-1]}")
print(f"Printing the first two values : {courses[:2]}")
x = slice(0, 2)
print(f"Printing with slice function : {courses[x]}")
#adding art to the end of the list
courses.append("Art")
print(f"Printing courses after adding art: {courses}")
print(f"Reversing the courses array : {courses[::-1]}")
my_name = "Balaji"
print(f"Reversing my_name : {my_name[::-1]}")
print(f"Joining everything using commas : {', '.join(courses)}")

# mutable example
list_1 = [1,2,3,4]
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 5
print(list_1)
print(list_2)

list_1.append(6)
print(list_1)
print(list_2)
