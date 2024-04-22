import argparse
#Displays current list of task to the user

class Task:    #Individual task in the to-do-list.
    def __init__(self, name, due_date=None, completed=False):   #Initializes a new task
        self.name = name #Name of task required.
        self.due_date = due_date  #Due date of the task.
        self.completed = completed  #Completion status of the task.

    def __repr__(self):  #Returns a string representation of the task object.
        return f'Task({self.name}, {self.due_date}, {self.completed})'


class ToDoList:  #class manages the list of tasks and provides methods to manipulate them
    def __init__(self): #Initializes an empty list to store tasks
        self.tasks = [] 

    def add_task(self, name, due_date=None): #Adds a new task to the list.
        task = Task(name, due_date) #Name of the task (required). #Due date of the task(Optional).
        self.tasks.append(task)

    def mark_completed(self, task_index): #Marks a task as completed based on its index in the list.
        if 0 <= task_index < len(self.tasks): #Index of the task to mark as completed.
            self.tasks[task_index].completed = True #Checks if the index is valid, then sets the completed attribute of the corresponding task to 
        else:
            print('Invalid task index')

    def remove_task(self, task_index): #Removes a task from the list based on its index.
        if 0 <= task_index < len(self.tasks): #Index of the task to remove.
            self.tasks.pop(task_index)
        else:
            print('Invalid task index')

    def view_tasks(self): #Displays the list of tasks with their completion status and due dates (if any).
        for i, task in enumerate(self.tasks):
            status = '[x]' if task.completed else '[ ]'
            print(f'{i+1}. {status} {task.name} ({task.due_date})')
#If there are no tasks in the list, it prints a message indicating that the list is empty.


def main():  #serves as the entry point of the program.
    todo_list = ToDoList() #Creates an instance of the ToDoList class.
    parser = argparse.ArgumentParser(description='To-Do List CLI')
    parser.add_argument('command', choices=['add', 'view', 'mark', 'remove'], help='Command to execute')
    parser.add_argument('args', nargs='*', help='Arguments for the command')
    args = parser.parse_args()

    if args.command == 'view':
        todo_list.view_tasks()

if __name__ == '__main__':
    main()