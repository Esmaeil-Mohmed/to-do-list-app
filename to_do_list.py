print("program started!")

to_do_list = []
print(to_do_list)


while True:

    user_command = input("Pls choose your command, (add, view, remove, exit): ")

    if user_command == "add":
        task = input("Pls enter your task: ")
        if task not in to_do_list:
            to_do_list.append(task)
            print("task added!")
            print(to_do_list)
        else:
            print("task already exists!")

    elif user_command == "view":
        if not to_do_list:
            print("no tasks to be viewed!")
        else:
            for task in to_do_list:
                print(task)

    elif user_command == "remove":
        if not to_do_list:
            print("no tasks to be removed!")
        else:
            task = input("Pls enter the task to be removed: ")
            if task in to_do_list:
                to_do_list.remove(task)
                print("task removed!")
                print(to_do_list)
            else:
                print("invalid name")

    elif user_command == "exit":
        answer = input("Are you sure (y/n): ")
        if answer == "y":
            break
        else:
            continue

    else:
        print("invalid command")