class Task:
    def __init__(self, name, due_date=None, completed=False):
        self.name = name
        self.due_date = due_date
        self.completed = completed

    def __repr__(self):
        return f'Task({self.name}, {self.due_date}, {self.completed})'


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date=None):
        task = Task(name, due_date)
        self.tasks.append(task)

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
        else:
            print('Invalid task index')

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
        else:
            print('Invalid task index')

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = '[x]' if task.completed else '[ ]'
            print(f'{i+1}. {status} {task.name} ({task.due_date})')


def main():
    todo_list = ToDoList()
    while True:
        print('\nTo-Do List:')
        todo_list.view_tasks()
        print('1. Add task')
        print('2. Mark completed')
        print('3. Remove task')
        print('4. Quit')
        option = int(input('Choose an option: '))
        if option == 1:
            name = input('Enter task name: ')
            due_date = input('Enter task due date (optional): ')
            todo_list.add_task(name, due_date)
        elif option == 2:
            index = int(input('Enter task index to mark as completed: ')) - 1
            todo_list.mark_completed(index)
        elif option == 3:
            index = int(input('Enter task index to remove: ')) - 1
            todo_list.remove_task(index)
        elif option == 4:
            break
        else:
            print('Invalid option, try again')


if __name__ == '__main__':
    main()