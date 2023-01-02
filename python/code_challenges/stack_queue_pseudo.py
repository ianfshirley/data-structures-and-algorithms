from data_structures.stack import Stack


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class PseudoQueue:
    """
    create a pseudoqueue class to implement standard queue interface, internally using 2 stack instances to create and manage the queue
    """

    def __init__(self):
        # self.front = None
        # self.rear = None
        stack_1 = Stack()
        stack_2 = Stack()

    def enqueue(self, value):
        #peek to see if stack 1 has a self.top value
        if stack_1.peek():
            stack_1.pop()

    def dequeue(self):
        pass
