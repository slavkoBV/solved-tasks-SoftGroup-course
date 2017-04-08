#! /usr/bin/env python3

from datetime import datetime
import os
from collections import OrderedDict


class Task:
    def __init__(self, content):
        self.content = content
        self.deadline = ''
        self.comment = ''
        self.priority = ''
        self.done = False
        self.date_create = datetime.now()

    def set_deadline(self, deadline):
        self.deadline = deadline

    def comment_task(self, comment):
        self.comment = comment

    def set_task_priority(self, priority):
        self.priority = priority

    def update_task(self, new_content):
        self.content = new_content

    def toggle_done(self):
        self.done = not self.done

    def __repr__(self):
        return 'Task: {0} - {1} - {2}'.format(self.content, 'DONE' if self.done else 'NOT DONE',
                                              self.deadline)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.content, 'DONE' if self.done else 'NOT DONE',
                                        self.deadline)


class TodoList(list):
    def __init__(self):
        super().__init__()
        self.tasks = []

    def add_task(self, new_task):
        """Add new task"""
        self.tasks.append(Task(new_task))

    def remove_task(self, index):
        """Remove Task with index"""
        del self.tasks[int(index)]

    def modify_task(self, index, attribute, value):
        """Modify task"""
        if attribute == 'u':
            self.tasks[index].update_task(value)
        elif attribute == 'd':
            self.tasks[index].toggle_done()
        elif attribute == 's':
            self.tasks[index].set_deadline(value)
        elif attribute == 'c':
            self.tasks[index].comment_task(value)
        elif attribute == 'p':
            self.tasks[index].set_task_priority(value)

    def show_list(self):
        """Show TODO list"""
        if len(self.tasks) != 0:
            print('{0:=^34}{1:^11}{2:=^35}'.format('=', 'TODO LIST', '='))
            print('{0:=^80}'.format('='))
            print('{0:^2}{1:^20}{2:^18}{3:^23}{4:^11}{5:^6}'.format('#', 'Task', 'Deadline', 'Comment', 'Priority',
                                                                    'Done'))
            print('{0:=^80}'.format('='))
            for ind, task in enumerate(self.tasks):
                print('{0:^2}{1:^20}{2:^18}{3:^23}{4:^10}{5:^7}'.format(ind, task.content, task.deadline,
                                                                        task.comment, task.priority,
                                                                        'True' if task.done else 'False'))
            print('\n' + '=' * 80 + '\n')

    def __repr__(self):
        return 'TODO: {}'.format(self.tasks)


def clear():
    """Clear the display"""
    os.system('cls' if os.name == 'nt' else 'clear')


def mainloop():
    """Explore task scheduler"""
    schedule = TodoList()
    menu = OrderedDict([
        ('a', schedule.add_task),
        ('r', schedule.remove_task),
        ('m', schedule.modify_task)
    ])

    sub_menu = OrderedDict([
        ('u', 'Update task (up to 18 symbols)'),
        ('d', 'Mark task as done (press "Enter")'),
        ('s', 'Set task deadline (ex. 2017-04-08 18:00)'),
        ('c', 'Comment task (up to 21 symbols)'),
        ('p', 'Set task priority (ex. 1 - 10)')
    ])

    choice = None
    while choice != 'q':
        clear()
        schedule.show_list()
        for key, value in menu.items():
            print('{} - {}'.format(key, value.__doc__))
        print('q - Quit')

        choice = input('\nMake choice: ')
        if choice in menu:
            if choice == 'm':
                print(menu[choice].__doc__, ':')
                for key, value in sub_menu.items():
                    print('{} - {}'.format(key, value))
                print(' q - Back to Main')
                action = input('\nChoose action: ')
                if action.lower().strip() in sub_menu:
                    try:
                        index = int(input('Choose task index: '))
                        value = input('Input new value for modifying attribute:')
                        print(action)
                        schedule.modify_task(index, action, value)
                    except (ValueError, IndexError):
                        pass
                continue
            try:
                print(menu[choice].__doc__, ':', end=' ')
                parameter = input()
                menu[choice](parameter)
            except (ValueError, IndexError):
                continue


if __name__ == '__main__':
    mainloop()
