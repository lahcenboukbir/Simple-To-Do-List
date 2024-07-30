def add_task(tasks):
    # Prompt the user to enter the task description
    task = input("Enter task: ")
    # Append the task description to the tasks list
    tasks.append(task)

def view_tasks(tasks):
    print("\nTasks:")
    # Loop through each task in the list and print the task with its index
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def delete_task(tasks):
    # Display the current tasks
    view_tasks(tasks)
    # Prompt the user to enter the task number to delete
    index = int(input("Enter task number to delete: ")) - 1
    # Check if the entered index is valid
    if index >= 0 and index < len(tasks):
        # Remove the task from the list and store the removed task
        removed_task = tasks.pop(index)
        # Print the removed task
        print(f"Deleted task: {removed_task}")
    else:
        # Print an error message if the index is invalid
        print("Invalid task number.")

def main():
    # Initialize an empty list to store tasks
    tasks = []

    while True:
        # Display menu options
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        # Prompt the user to choose an option
        choice = input("Choose an option: ")
        
        # Handle the user's choice
        if choice == "1":
            # Call add_task function to add a new task
            add_task(tasks)
        elif choice == "2":
            # Call view_tasks function to display all tasks
            view_tasks(tasks)
        elif choice == "3":
            # Call delete_task function to delete a task
            delete_task(tasks)
        elif choice == "4":
            # Exit the loop and terminate the program
            break
        else:
            # Print an error message for invalid choice
            print("Invalid choice. Please try again.")

# Call the main function to run the program
main()
