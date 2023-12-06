# todo_app.py
from task_manager import TaskManager

class ToDoApp:
    def __init__(self):
        print("Program started!")
        self.task_manager = TaskManager()

    def run(self):
        while True:
            user_command = input("Please choose your command (add, view, remove, exit): ")

            if user_command == "add":
                self.task_manager.add_task()
            elif user_command == "view":
                self.task_manager.view_tasks()
            elif user_command == "remove":
                self.task_manager.remove_task()
            elif user_command == "exit":
                if self.task_manager.exit_program():
                    break
            else:
                print("Invalid command")


if __name__ == "__main__":
    todo_app = ToDoApp()
    todo_app.run()
