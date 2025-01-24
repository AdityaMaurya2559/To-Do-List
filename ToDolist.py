# Simple To-Do List in Python

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in your to-do list!")
    else:
        print("\nYour To-Do List:")
        for i, (task, done) in enumerate(tasks, start=1):
            status = "✓" if done else "✗"
            print(f"{i}. [{status}] {task}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append((task, False))
    print("Task added successfully!")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            task, _ = tasks[task_num]
            tasks[task_num] = (task, True)
            print(f"Task {task_num + 1} marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task[0]}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
