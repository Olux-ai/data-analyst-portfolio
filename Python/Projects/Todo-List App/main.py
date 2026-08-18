#Create an empty list to store the tasks and their status
todo_list = []


#Function to Add a New task to the todo list
def add_task():
  task = input("Enter the task: ")
  todo_list.append({"task": task, "status": "Pending Task"})
  print("New Task Added Successfully!\n")

#Function to View all Tasks  
def view_tasks():
  print("Your Todo List:")
  if len(todo_list) == 0:
    print("No tasks found.")
  else:
    for i, task in enumerate(todo_list,1):
      print(f"{i}: [{task['status']}] - {task['task']}")

  print("\n")
  

  
#Function to Display a Menu
def display_menu():
  while(True):
    print("*** Main Menu ***")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Remove a Task")
    print("4. Mark a Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
      add_task()
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      remove_task()
    elif choice == '4':
      mark_done()
    elif choice == '5':
      print("Exiting the application...")
      exit()
    else:
      print("Invalid choice. Please try again.")

display_menu()

