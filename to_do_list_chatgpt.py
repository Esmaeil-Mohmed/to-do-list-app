def add_task(to_do_list):
    task = input("Please enter your task: ")
    if task not in to_do_list:
        to_do_list.append(task)
        print("Task added!")
        print_tasks(to_do_list)
    else:
        print("Task already exists!")

def view_tasks(to_do_list):
    if not to_do_list:
        print("No tasks to be viewed!")
    else:
        print_tasks(to_do_list)

def remove_task(to_do_list):
    if not to_do_list:
        print("No tasks to be removed!")
    else:
        task = input("Please enter the task to be removed: ")
        if task in to_do_list:
            to_do_list.remove(task)
            print("Task removed!")
            print_tasks(to_do_list)
        else:
            print("Invalid task name")

def exit_program(to_do_list):
    answer = input("Are you sure? (y/n): ")
    if answer.lower() == "y":
        return True
    return False

def print_tasks(tasks):
    if tasks:
        print("Tasks:", ", ".join(tasks))
    else:
        print("No tasks.")

print("Program started!")

to_do_list = []

while True:
    user_command = input("Please choose your command (add, view, remove, exit): ")

    if user_command == "add":
        add_task(to_do_list)
    elif user_command == "view":
        view_tasks(to_do_list)
    elif user_command == "remove":
        remove_task(to_do_list)
    elif user_command == "exit":
        if exit_program(to_do_list):
            break
    else:
        print("Invalid command")
