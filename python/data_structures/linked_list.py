class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        adds a new node with a value to the head of the list - with an O(1) time performance
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        """
        indicates whether a value exists as a Node's value somewhere within the list
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def insert_before(self, before, value):
        current = self.head
        previous = None
        try:
            while current.value is not before:
                previous = current
                current = current.next
            new_node = Node(value)
            new_node.next = current
            if previous is not None:
                previous.next = new_node
            if previous is None:
                self.head = new_node
        except Exception as e:
            raise TargetError(e)

    def insert_after(self, after, value):
        current = self.head
        try:
            while current.value is not after:
                current = current.next
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
        except Exception as e:
            raise TargetError(e)

    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append("{ " + str(current.value) + " }")
            current = current.next
        if len(values) == 0:
            return "NULL"
        return " -> ".join(values) + " -> NULL"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class TargetError(Exception):
    pass
