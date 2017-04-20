from datetime import datetime
import pickle


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
