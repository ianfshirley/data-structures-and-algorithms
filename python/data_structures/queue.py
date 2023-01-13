from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Initiates a queue with Nodes to be added (enqueue) or removed (dequeue) following the FIFO / LILO principles. The
    first node to be added will be the first one out. The last node added will be the last one out. Like queueing
    for a movie.
    """

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        if self.back:
            self.back.next = Node(value)
            self.back = self.back.next
            return
        self.back = self.front = Node(value)

    def dequeue(self):
        try:
            if self.front == self.back:
                dequeued = self.front
                self.front = self.back = None
                return dequeued.value
            dequeued = self.front
            self.front = self.front.next
            return dequeued.value
        except Exception as e:
            raise InvalidOperationError(e)

    def peek(self):
        try:
            return self.front.value
        except Exception as e:
            raise InvalidOperationError(e)

    def is_empty(self):
        return self.front is None
