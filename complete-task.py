import argparse

class Task: #defines a class named Task, which represents individual tasks in the To-Do List.
    def __init__(self, name, due_date=None, completed=False): #defines the constructor method for the Task class.
        self.name = name  #Name of the task.
        self.due_date = due_date #Due date of the task.
        self.completed = completed #Completion status of the project.

    def __repr__(self): #Defines the __repr__ method for the Task class, which returns a string representation of the task object.
        return f'Task({self.name}, {self.due_date}, {self.completed})' #Returns a string representation of the task object, including its name, due date, and completion status.


class ToDoList: #Defines a class named ToDoList, which represents the list of tasks in the To-Do List application.
    def __init__(self): #Defines the constructor method for the ToDoList class.
        self.tasks = [] #Initializes the instance variable tasks as an empty list.

    def add_task(self, name, due_date=None): #Defines the add_task method for the ToDoList class, which adds a new task to the list.
        task = Task(name, due_date) #This line creates a new Task object with the provided name and due date.
        self.tasks.append(task) #Appends the newly created task to the tasks list.

    def mark_completed(self, task_index): #Defines the mark_completed method for the ToDoList class, which marks a task as completed and removes it from the list.
        if 0 <= task_index < len(self.tasks):#checks if the provided task index is within the valid range of task indices in the list.
            self.tasks[task_index].completed = True
            self.tasks.pop(task_index)
        else:
            print('Invalid task index') #Prints a message indicating that the provided task index is invalid if it is not within the valid range.

    def view_tasks(self): #Defines the view_tasks method for the ToDoList class, which displays the list of tasks.
        for i, task in enumerate(self.tasks): #Iterates over the tasks in the list, along with their corresponding indices.
            status = '[x]' if task.completed else '[ ]' #Determines the status of the task (completed or not) and assigns the appropriate status indicator ([x] for completed, [ ] for not completed).
            print(f'{i+1}. {status} {task.name} ({task.due_date})') #Prints the index, status, name, and due date (if available) of each task in the list.


def main(): #Defines the main function, which serves as the entry point of the program.
    todo_list = ToDoList() #Creates an instance of the ToDoList class to manage the list of tasks.
    parser = argparse.ArgumentParser(description='To-Do List CLI') #Creates an argument parser object using argparse, with a description for the program.
    parser.add_argument('command', choices=['add', 'view', 'complete', 'remove'], help='Command to execute')#add command-line arguments to the parser.
    parser.add_argument('args', nargs='*', help='Arguments for the command') #Adds command-line arguments to the parser.
    args = parser.parse_args()

    if args.command == 'add':
        name, due_date = args.args
        todo_list.add_task(name, due_date)
    elif args.command == 'view':
        todo_list.view_tasks()
    elif args.command == 'complete':
        index = int(args.args[0])
        todo_list.mark_completed(index - 1)
    elif args.command == 'remove':
        index = int(args.args[0])
        todo_list.tasks.pop(index - 1)
    else:
        print('Invalid command')


if __name__ == '__main__':
    main()