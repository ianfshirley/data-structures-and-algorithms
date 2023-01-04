from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def enqueue(self, value):
        self.queue1.enqueue(value)

    def dequeue(self, preference):
        result = None
        while self.queue1.front is not None:
            if self.queue1.front.value.type == preference and result is None:
                result = self.queue1.front.value
            else:
                self.queue2.enqueue(self.queue1.front.value)
            self.queue1.front = self.queue1.front.next
        self.queue1 = self.queue2
        self.queue2 = Queue()
        return result


class Dog:
    def __init__(self):
        self.type = "dog"


class Cat:
    def __init__(self):
        self.type = "cat"
