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


class TargetError:
    pass
