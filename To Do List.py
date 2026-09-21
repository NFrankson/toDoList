
todoList = []
maxLengthList = 6


def todo_input():
    while len(todoList) < maxLengthList:
        item = input("Enter your task you need to do (Type 'Done' if you are done): ")
        if item == "Done":
            print("You are done!")
            break
        todoList.append(item)
    print("That's your To Do List!")
    print(todoList)

def todo_remove():
    task_to_remove = input("Enter the task you want to remove: ")
    if task_to_remove == "List":
        print(todoList)
    todoList.remove(task_to_remove)
    print(f"You have removed the item {task_to_remove}")
    print(todoList)

def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Add to your To Do List")
        print("2. Remove from your To Do List")
        print("3. Show my list")
        print("4. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            todo_input()
        elif choice == '2':
            todo_remove()
        elif choice == '3':
            print(todoList)
        elif choice == '4':
            print("You are leaving, goodbye!")
            break
        else:
            print("Invalid selction. Please choose a valid option.")

main_menu()   



