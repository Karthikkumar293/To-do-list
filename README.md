# To-Do List App by Karthik

This Python script is a simple command-line To-Do List application that allows you to add, update, view, and manage tasks interactively.

## Prerequisites

- Python 3.x installed on your system.

## Usage

1. **Create the Python Script:**

    Save the following code in a file named `todo_list.py`:

    ```python
    def task():
        tasks = []  # Empty list to hold tasks
        print("WELCOME TO TO DO LIST APP MADE BY KARTHIK")
        
        total_tasks = int(input("Enter how many tasks you want to add: "))
        for i in range(1, total_tasks + 1):
            task_name = input(f"Enter task {i}: ")
            tasks.append(task_name)
        
        print(f"Today's tasks are: {tasks}")
        
        while True:
            print("\nChoose an operation:")
            print("1 - Add a task")
            print("2 - Update a task")
            print("3 - View tasks")
            print("4 - Exit")
            
            operation = int(input("Enter your choice (1/2/3/4): "))
            
            if operation == 1:
                add_task = input("Enter the task you want to add: ")
                tasks.append(add_task)
                print(f"Task '{add_task}' has been successfully added!")
            
            elif operation == 2:
                updated_task = input("Enter the task you want to update: ")
                if updated_task in tasks:
                    ind = tasks.index(updated_task)
                    new_task = input("Enter your new task: ")
                    tasks[ind] = new_task
                    print(f"Task '{updated_task}' has been successfully updated to '{new_task}'!")
                else:
                    print("Task not found!")
            
            elif operation == 3:
                print(f"Current tasks: {tasks}")
            
            elif operation == 4:
                print("EXITING TO DO LIST APP MADE BY KARTHIK!")
                break
            
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")

    task()
    ```

2. **Run the Script:**

    To run the Python script, use the following command in your terminal:

    ```bash
    python todo_list.py
    ```

3. **Follow the Instructions:**

    - **Add Initial Tasks:** When prompted, enter the number of tasks you want to add and input each task one by one.
    - **Choose an Operation:** After entering initial tasks, the script provides options to add more tasks, update existing tasks, view all tasks, or exit the app.
    - **Perform Operations:** Enter the corresponding number (1-4) to perform the desired operation.

## Notes

- Make sure Python 3.x is installed and properly configured on your system to run this script.
- The script will continue running until you choose to exit by selecting option 4.

---

By following these steps, you can manage your tasks using this simple command-line To-Do List application.
