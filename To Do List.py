
todoList = []
maxLengthList = 10


def todo_input():
    while len(todoList) < maxLengthList:
        item = input("Enter your task you need to do: ")
        todoList.append(item)
    print("That's your To Do List!")
    print(todoList)

todo_input()

def todo_remove():
    todoList.remove(input("Enter the task  you want to remove: "))
    print("You have removed the item")

