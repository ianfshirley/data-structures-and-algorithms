from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            return
        old = self.top
        self.top = Node(value)
        self.top.next = old

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        popped = self.top
        self.top = self.top.next
        return popped.value

    def peek(self):
        if self.top is not None:
            return self.top.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False
