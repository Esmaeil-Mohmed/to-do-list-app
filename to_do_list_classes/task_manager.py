# task_manager.py

class TaskManager:
    def __init__(self):
        self.to_do_list = []

    def add_task(self):
        task = input("Please enter your task: ")
        if task not in self.to_do_list:
            self.to_do_list.append(task)
            print("Task added!")
            self.print_tasks()
        else:
            print("Task already exists!")

    def view_tasks(self):
        if not self.to_do_list:
            print("No tasks to be viewed!")
        else:
            self.print_tasks()

    def remove_task(self):
        if not self.to_do_list:
            print("No tasks to be removed!")
        else:
            task = input("Please enter the task to be removed: ")
            if task in self.to_do_list:
                self.to_do_list.remove(task)
                print("Task removed!")
                self.print_tasks()
            else:
                print("Invalid task name")

    def exit_program(self):
        answer = input("Are you sure? (y/n): ")
        if answer.lower() == "y":
            return True
        return False

    def print_tasks(self):
        if self.to_do_list:
            print("Tasks:", ", ".join(self.to_do_list))
        else:
            print("No tasks.")
