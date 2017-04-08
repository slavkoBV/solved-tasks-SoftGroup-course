class Stack(list):
    def __init__(self, size):
        super().__init__(self)
        self.items = []
        self.size = size

    def push(self, item):
        if len(self.items) > self.size:
            raise Exception('Stack overflow')
        else:
            self.items.append(item)

    def get_item(self):
        if len(self.items) >= 1:
            return self.items.pop()
        else:
            raise Exception('Stack is empty')

    def is_empty(self):
        return False if len(self.items) > 0 else True

    def is_full(self):
        return False if len(self.items) < self.size else True

    def __repr__(self):
        return 'Stack({0.items}, {1})'.format(self, len(self.items))

    def __str__(self):
        return '({0.items}, {1})'.format(self, len(self.items))
