import os
from collections import OrderedDict


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
