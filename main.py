import os
from storage import *


def main():
    tasks = load_tasks("tasks.txt")
    interface(tasks)


def interface(tasks):
    while True:
        clear()
        print("--------------------------")
        print("What would you like to do?")
        print("--------------------------")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Quit")
        print("--------------------------")
        choice = input("Type '1' '2' '3' or '4': ").strip().lower()

        if choice == "1":
            clear()
            task = input("Type your task: ")
            tasks.append(task)
            save_tasks(tasks, "tasks.txt")
        elif choice == "2":
            clear()
            display_tasks(tasks)
            input("Press ENTER to return to menu")
        elif choice == "3":
            if len(tasks) == 0:
                clear()
                input("ToDoList is empty, press ENTER to return to menu")
            else:
                clear()
                display_tasks(tasks)
                deleted_num = get_delete_index(tasks)
                clear()
                print(f"Deleted task number {deleted_num}")
                print("Updated list:")
                display_tasks(tasks)
                save_tasks(tasks, "tasks.txt")
                input("Press ENTER to return to menu")
        elif choice == "4":
            break

    clear()
    print("--------------------------")
    print("Closing app...")
    print("--------------------------")


def display_tasks(tasks):
    print("--------------------------")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print("--------------------------")


def get_delete_index(tasks):
    while True:
        try:
            delete_num = int(input("Type number of task you would like to delete: "))
            tasks.pop(delete_num - 1)
            return delete_num
        except IndexError:
            print("Invalid input. Please enter a number that matches a task.")
        except ValueError:
            print("Invalid input. Please enter a number that matches a task.")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()



