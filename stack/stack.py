class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(len(self.items))

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
