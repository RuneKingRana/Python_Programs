students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print(f"Enter student number {i+1}'s details: ")
    name = input("Name: ")
    roll = input("Roll number: ")
    marks = input("marks: ")
    students.append((name, roll, marks))

print("Student list: ")
for s in students:
    print("Name: {}, Roll number: {}, Marks: {}".format(s[0], s[1], s[2]))