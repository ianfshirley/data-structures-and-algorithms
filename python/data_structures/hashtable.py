from data_structures.linked_list import Node, LinkedList


class Hashtable:
    """
    Put docstring here
    """


    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size


    def _hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        hash = (hash * 599) % self.size
        return hash

    def set(self):
        # method body here
        pass


    def get(self):
        # method body here
        pass


    def has(self):
        # method body here
        pass


    def keys(self):
        # method body here
        pass