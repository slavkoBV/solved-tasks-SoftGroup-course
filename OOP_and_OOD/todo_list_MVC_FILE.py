#! /usr/bin/env python3

from datetime import datetime
import os
from collections import OrderedDict
import pickle


# Model ###################################################################################
class Task:
    def __init__(self, content='', deadline=None, priority=None, comment=None):
        self.content = content
        self._deadline = deadline
        self._priority = priority
        self.comment = comment
        self.done = False
        self.date_create = datetime.now()

    @property
    def deadline(self):
        return self._deadline if self._deadline else None

    @deadline.setter
    def deadline(self, deadline):
        if deadline:
            date = datetime.strptime(deadline, '%Y-%m-%d')
            if date >= self.date_create:
                self._deadline = date

    @property
    def priority(self):
        return self._priority if self._priority else None

    @priority.setter
    def priority(self, priority):
        self._priority = priority

    def comment_task(self, comment):
        self.comment = comment

    def toggle_done(self):
        self.done = not self.done

    def __str__(self):
        return 'Task: {0}: deadline - {1}, priority - {2}, done - {3}'.format(self.content, self.deadline,
                                                                              self.priority, self.done)

    def __repr__(self):
        return 'Task: {0}: deadline - {1}, priority - {2}, done - {3}'.format(self.content, self.deadline,
                                                                              self.priority, self.done)


class TodoList(list):
    def __init__(self):
        super().__init__()
        self.tasks = []

    def add_task(self, content, deadline=None, priority=None, comment=None):
        """Add new task"""
        self.tasks.append(Task(content, deadline, priority, comment))

    def remove_task(self, index):
        """Remove Task with index"""
        del self.tasks[index]

    def get_tasks(self):
        """Return enumerated list of all tasks"""
        task_list = []
        for index, task in enumerate(self.tasks):
            task_list.append([index, task.content, task.deadline, task.comment, task.priority, task.done])
        return task_list

    def save_list(self, filename):
        dbfile = open(filename, 'wb')
        pickle.dump(self.tasks, dbfile)
        dbfile.close()

    def load_list(self, filename):
        try:
            dbfile = open(filename, 'rb')
            self.tasks = pickle.load(dbfile)
        except FileNotFoundError:
            pass

    def __str__(self):
        return 'Todo: {}'.format(self.tasks)

    def __repr__(self):
        return 'Todo: {}'.format(self.tasks)


################################################################################################################


class Controller:
    def __init__(self):
        self.model = TodoList()
        self.view = View()
        self.choice = None

    def manager(self):
        self.view.clear()
        records = self.model.get_tasks()  # Get all tasks
        self.view.show_list(records)      # View all tasks
        self.view.show_main_menu()
        self.choice = self.view.input_value('your choice')

        # User choice handler for list processing
        if self.choice == 'a':            # add new task to list
            task = self.view.input_value('new task (task, deadline, priority, comment)')
            self.model.add_task(*(task.split(',')))
        elif (self.choice == 'r') and (len(records) != 0):   # remove task with index from list
            index = self.view.input_value('task index')
            try:
                self.model.remove_task(int(index))
            except (IndexError, ValueError):
                pass
        elif self.choice == 'w':                             # write list to file
            filename = self.view.input_value('filename')
            self.model.save_list(filename)
        elif self.choice == 'l':                             # load list from file
            filename = self.view.input_value('filename')
            self.model.load_list(filename)
        elif (self.choice == 'm') and (len(records) != 0):   # modify list
            self.view.clear()
            self.view.show_sub_menu()
            sub_choice = self.view.input_value('your choice')
            # User choice handler for modifying of chosen task
            try:
                index = int(self.view.input_value('task index'))
                if sub_choice == 'u':                              # update task
                    value = self.view.input_value('updated task')
                    self.model.tasks[index].content = value
                elif sub_choice == 'd':                            # switch complete the task
                    self.model.tasks[index].toggle_done()
                elif sub_choice == 's':                            # set task deadline
                    value = self.view.input_value('new deadline')
                    self.model.tasks[index].deadline = value
                elif sub_choice == 'c':                            # comment the task
                    value = self.view.input_value('comment')
                    self.model.tasks[index].comment_task(value)
                elif sub_choice == 'p':                             # set task priority
                    value = self.view.input_value('task priority')
                    self.model.tasks[index].priority = value
            except (IndexError, ValueError):
                pass


################################################################

class View:
    menu = OrderedDict([
        ('a', 'Add new task'),
        ('r', 'Remove task'),
        ('m', 'Modify task'),
        ('w', 'Save to file'),
        ('l', 'Load list from file'),
    ])
    sub_menu = OrderedDict([
        ('u', 'Update task (up to 18 symbols)'),
        ('d', 'Mark task as done'),
        ('s', 'Set task deadline (ex. 2017-04-08 18:00)'),
        ('c', 'Comment task (up to 21 symbols)'),
        ('p', 'Set task priority (ex. 1 - 10)')
    ])

    @staticmethod
    def clear():
        """Clear the display"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def show_main_menu():
        """Show main menu of program"""
        for key, value in View().menu.items():
            print('{} - {}'.format(key, value))
        print('q - Quit')

    @staticmethod
    def show_sub_menu():
        """Show sub menu to modify tasks"""
        for key, value in View().sub_menu.items():
            print('{} - {}'.format(key, value))
        print(' q - Back to Main')

    @staticmethod
    def input_value(parameter):
        """Interface to user input of different parameters"""
        return input('Input {}: '.format(parameter))

    @staticmethod
    def show_list(data):
        """Show TODO list"""
        print('{0:=^34}{1:^11}{2:=^35}'.format('=', 'TODO LIST', '='))
        print('{0:=^80}'.format('='))
        print('{0:^2}{1:^20}{2:^18}{3:^23}{4:^11}{5:^6}'.format('#', 'Task', 'Deadline', 'Comment', 'Priority',
                                                                'Done'))
        print('{0:=^80}'.format('='))
        if len(data) != 0:
            for record in data:
                print('{0!s:^2}{1!s:^20}{2!s:^18}{3!s:^23}{4!s:^10}{5!s:^7}'.format(*(i for i in record)))
            print('\n' + '=' * 80 + '\n')
###############################################################################################


if __name__ == '__main__':
    control = Controller()
    while control.choice not in ('Q', 'q'):
        control.manager()
    else:
        print('Bye')
