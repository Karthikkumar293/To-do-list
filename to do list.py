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
           
            

                    



                
