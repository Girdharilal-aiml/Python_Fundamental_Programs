def todo_list():
    tasks = []
    
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            tasks.append({"task": task, "completed": False})
            print("Task added!")
            
        elif choice == '2':
            for i, task in enumerate(tasks, 1):
                status = "✓" if task['completed'] else "✗"
                print(f"{i}. [{status}] {task['task']}")
                
        elif choice == '3':
            idx = int(input("Enter task number: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]['completed'] = True
                print("Task marked complete!")
            else:
                print("Invalid task number!")
                
        elif choice == '4':
            idx = int(input("Enter task number: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                print("Task deleted!")
            else:
                print("Invalid task number!")
                
        elif choice == '5':
            break