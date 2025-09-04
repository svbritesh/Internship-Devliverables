import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

# Show menu
def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

# Main program
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            if not tasks:
                print("No tasks yet!")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added!")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
                continue

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                index = int(input("Enter task number to delete: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Thank You ")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
