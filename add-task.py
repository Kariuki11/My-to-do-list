import argparse  #The argparse module makes it easy to write user-friendly command-line interfaces.

class Task:
    def __init__(self, name, due_date=None, completed=False): #Initializes an empty list to store tasks.
        self.name = name #Name of the task.
        self.due_date = due_date #Due date of the task(optional).
        self.completed = completed #Completion status.

    def __repr__(self): #Returns a string representation of the task object.
        return f'Task({self.name}, {self.due_date}, {self.completed})'


class ToDoList: #Initializes an empty list to store tasks.
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date=None): #Adds a new task to the list.
        task = Task(name, due_date) #Name of the task #Due date of the task.
        self.tasks.append(task)

    def mark_completed(self, task_index): #Marks a task as completed based on its index in the list.
        if 0 <= task_index < len(self.tasks): #Index of the task to mark as completed.
            self.tasks[task_index].completed = True
        else:
            print('Invalid task index')

    def remove_task(self, task_index): #Remove a task from the list based on it's Index.
        if 0 <= task_index < len(self.tasks): #Index of task to remove.
            self.tasks.pop(task_index) #Checks if the index is valid, then removes the task from the list using the pop() method.
        else:
            print('Invalid task index')

    def view_tasks(self): #Displays the list of tasks with their completion status and due dates (if any).
        for i, task in enumerate(self.tasks):
            status = '[x]' if task.completed else '[ ]'
            print(f'{i+1}. {status} {task.name} ({task.due_date})')


def main():
    todo_list = ToDoList() #Creates an instance of the ToDoList class.
    parser = argparse.ArgumentParser(description='To-Do List CLI') #Sets up the command-line argument parser using argparse.
    parser.add_argument('command', choices=['add', 'view', 'mark', 'remove'], help='Command to execute')
    parser.add_argument('args', nargs='*', help='Arguments for the command')
    args = parser.parse_args()

    if args.command == 'add':
        name, due_date = args.args
        todo_list.add_task(name, due_date)
    elif args.command == 'view':
        todo_list.view_tasks()

if __name__ == '__main__':
    main()