import argparse  #Module to parse command-line arguments.
import json  #Works on Json data.

class Task:
    def __init__(self, name, due_date=None, completed=False):
        self.name = name
        self.due_date = due_date
        self.completed = completed
#Defines a class named Task, representing individual tasks in the to-do list.
#It initializes three attributes: name, due_date, and completed.

    def __repr__(self):
        return f'Task({self.name}, {self.due_date}, {self.completed})'


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
#Defines a class named ToDoList, representing the entire to-do list.
#It initializes an empty list tasks to store tasks and loads tasks from a JSON file when instantiated.


    def add_task(self, name, due_date=None):#Input validation is performed to ensure that the task name provided by the user is a non-empty string #error handling function
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Task name must be a non-empty string")
        task = Task(name, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.tasks.pop(task_index)
            self.save_tasks()
        else:
            raise IndexError("Task index is out of range")
#An indexError is raised if the provided task_index is out of range (i.e., less than 0 or greater than or equal to the length of the tasks list). #Error handling function.
#This mechanism ensures that users cannot attempt to mark a task as completed with an invalid index, preventing potential crashes or unexpected behavior.

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = '[x]' if task.completed else '[ ]'
            print(f'{i+1}. {status} {task.name} ({task.due_date})')

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            pass
#An attempt is made to load tasks from a JSON file named tasks.json.
#If the file is not found (eg, a FileNotFoundError occurs), the exception is caught, and the method gracefully handles the situation by passing silently.
#This prevents the script from crashing if the tasks file is missing, allowing the application to continue execution without interruption.   #Error handling.


def main():
    todo_list = ToDoList()
    parser = argparse.ArgumentParser(description='To-Do List CLI')