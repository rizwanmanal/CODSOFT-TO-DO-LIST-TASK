class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def update_task(self, index, new_task):
        self.tasks[index] = new_task
        print(f"Task updated: {new_task}")

    def delete_task(self, index):
        task = self.tasks.pop(index)
        print(f"Task deleted: {task}")

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")


def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice =int(input("Enter your choice: "))

        if choice == 1:
            task = (input("Enter task: "))
            to_do_list.add_task(task)
        elif choice == 2:
            index = int(input("Enter index of task to update: "))
            new_task = input("Enter new task: ")
            to_do_list.update_task(index - 1, new_task)
        elif choice == 3:
            index = int(input("Enter index of task to delete: "))
            to_do_list.delete_task(index - 1)
        elif choice == 4:
            to_do_list.display_tasks()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()