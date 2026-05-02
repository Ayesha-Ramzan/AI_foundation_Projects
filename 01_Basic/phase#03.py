
#Student Record system
name = input("Name:")
marks = int(input("Marks:"))

print("=== Student Record ===")
print("Name  :", name)
print("Marks :", marks)

if marks >= 80:
    print("Grade : A")
elif marks >= 60:
    print("Grade : B")
elif marks >= 40:
    print("Grade : C")
else:
    print("Grade : Fail")


 #TO-DO List app
todos = []

print("=== To Do List ===")

task = input("Add task: ")
todos.append(task)
print("Added:", todos)

task = input("Add another task: ")
todos.append(task)
print("Added:", todos)

remove = input("Delete task: ")
todos.remove(remove)
print("Remaining:", todos)   