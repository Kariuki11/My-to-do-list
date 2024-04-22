import argparse
import json #Used for encoding and decoding JSON data.

class Task: #These lines defines a class named `Task`, which represents individual tasks in the To-Do List.
    def __init__(self, name, due_date=None, completed=False): #defines the constructor method for the Task class.
        self.name = name #Name of the task
        self.due_date = due_date #Due date of the task
        self.completed = completed #Completion status of the project.

    def __repr__(self): #defines the __repr__ method for the Task class, which returns a string representation of the task object.
        return f'Task({self.name}, {self.due_date}, {self.completed})'
# The above lines initialize the instance variables `name`, `due_date`, and `completed` with the values provided to the constructor.

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
#The above block defines a class named ToDoList, representing the entire to-do list.
#It initializes an empty list tasks to store tasks and loads tasks from a JSON file when instantiated.

    def add_task(self, name, due_date=None):
        task = Task(name, due_date)
        self.tasks.append(task)
        self.save_tasks()
#The above method adds a new task to the list with the provided name and due date (if any).
#It creates a Task object, appends it to the list, and saves the updated list to a JSON file.

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()
            self.tasks.pop(task_index)
        else:
            print('Invalid task index')
#The above method marks a task at a given index as completed and removes it from the list.
#It sets the completion status of the task, saves the updated list, and removes the task.

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = '[x]' if task.completed else '[ ]'
            print(f'{i+1}. {status} {task.name} ({task.due_date})')
#The above method displays all tasks in the list along with their index, completion status, name, and due date (if any).

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f)
#The above function serializes the list of tasks into JSON format and writes it to a file named tasks.json.

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            pass
#The method above loads tasks from the tasks.json file and assigns them to the tasks attribute.
#It handles the case where the file is not found by ignoring the exception.

def main():
    todo_list = ToDoList()
    parser = argparse.ArgumentParser(description='To-Do List CLI')
    parser.add_argument('command', choices=['add', 'view', 'complete', 'remove'], help='Command to execute')
    parser.add_argument('args', nargs='*', help='Arguments for the command')
    args = parser.parse_args()
#The main function is the entry point of the script.
#It creates a ToDoList instance, sets up an argument parser, and parses command-line arguments.

    if args.command == 'add':
        name, due_date = args.args
        todo_list.add_task(name, due_date)
#This block checks the provided command and executes corresponding actions based on the command and arguments.
#For example, if the command is 'add', it extracts the name and due date from arguments and adds a new task.
    elif args.command == 'view':
        todo_list.view_tasks()
#If the command is 'view', it calls the view_tasks method to display the tasks.
    elif args.command == 'complete':
        index = int(args.args[0])
        todo_list.mark_completed(index - 1)
#If the command is 'complete', it extracts the task index from arguments and marks the task as completed.
    elif args.command == 'remove':
        index = int(args.args[0])
        todo_list.tasks.pop(index - 1)
        todo_list.save_tasks()
#If the command is 'remove', it removes the task at the specified index and saves the updated list.
    else:
        print('Invalid command')
#This block handles the case where an invalid command is provided by printing a message.


#This line below ensures that the main function is executed when the script is run directly, not imported as a module.
if __name__ == '__main__':
    main()