"""
Goal: Build a program where users can add tasks (e.g., "Finish Python assignment")
to a list and view them
"""
# key skill : lists ( append and print loop)
# tasks list
print("This is my To-Do list")
Task = []
while True:
    Task.append(input("Enter your task : "))
    for i in range(len(Task)):
        print(i+1,"Task is :",Task[i])
    print("Do you want to add more task select Y, If you want to close program select N")
    choice = input("Enter Choice (Y/N)")
    if choice == 'N' :
        break
