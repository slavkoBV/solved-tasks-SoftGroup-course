from .model import TodoList
from .view import View


class Controller:
    def __init__(self):
        self.model = TodoList()
        self.view = View()
        self.choice = None

    def manager(self):
        self.view.clear()
        records = self.model.get_tasks()  # Get all tasks
        self.view.show_list(records)  # View all tasks
        self.view.show_main_menu()
        self.choice = self.view.input_value('your choice')

        # User choice handler for list processing
        if self.choice == 'a':  # add new task to list
            task = self.view.input_value('new task (task, deadline, priority, comment)')
            self.model.add_task(*(task.split(',')))
        elif (self.choice == 'r') and (len(records) != 0):  # remove task with index from list
            index = self.view.input_value('task index')
            try:
                self.model.remove_task(int(index))
            except (IndexError, ValueError):
                pass
        elif self.choice == 'w':  # write list to file
            filename = self.view.input_value('filename')
            self.model.save_list(filename)
        elif self.choice == 'l':  # load list from file
            filename = self.view.input_value('filename')
            self.model.load_list(filename)
        elif (self.choice == 'm') and (len(records) != 0):  # modify list
            self.view.clear()
            self.view.show_sub_menu()
            sub_choice = self.view.input_value('your choice')
            # User choice handler for modifying of chosen task
            try:
                index = int(self.view.input_value('task index'))
                if sub_choice == 'u':  # update task
                    value = self.view.input_value('updated task')
                    self.model.tasks[index].content = value
                elif sub_choice == 'd':  # switch complete the task
                    self.model.tasks[index].toggle_done()
                elif sub_choice == 's':  # set task deadline
                    value = self.view.input_value('new deadline')
                    self.model.tasks[index].deadline = value
                elif sub_choice == 'c':  # comment the task
                    value = self.view.input_value('comment')
                    self.model.tasks[index].comment_task(value)
                elif sub_choice == 'p':  # set task priority
                    value = self.view.input_value('task priority')
                    self.model.tasks[index].priority = value
            except (IndexError, ValueError):
                pass
