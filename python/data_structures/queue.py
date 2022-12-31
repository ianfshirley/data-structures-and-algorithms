from invalid_operation_error import InvalidOperationError
import pytest


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Put docstring heree
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # check to see if queue is empty
        if self.rear:
            # change 'next' for old rear from None to the new node
            self.rear.next = Node(value)
            # set the rear to be the new node
            self.rear = self.rear.next
            return
        self.rear = self.front = Node(value)

    def dequeue(self, value):
        dequeued = self.front
        self.front.next = self.front
        return dequeued.value

    def peek(self):
        pass

    def is_empty(self):
        pass
