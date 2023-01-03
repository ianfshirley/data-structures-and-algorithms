from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        if self.stack2.top is not None:
            while self.stack2.top is not None:
                item = self.stack2.pop()
                self.stack1.push(item)
        self.stack1.push(value)

    def dequeue(self):
        if self.stack1.top is not None:
            while self.stack1.top is not None:
                item = self.stack1.pop()
                self.stack2.push(item)
        result = self.stack2.pop()
        return result
