from data_structures.linked_list import Node, LinkedList


class Hashtable:
    
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size


    def _hash(self, key):
        """
        Takes in a string called the 'key', and returns a integer representing an index of _buckets
        """
        hash = 0
        for char in key:
            hash += ord(char)
        hash = (hash * 599) % self.size
        return hash

    def set(self, key, value):
        """
        given a key/value pair, hash the key, and insert the pair into the correct bucket (the bucket is the index returned by hash function)
        """
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]

        if not bucket:
            self._buckets[hashed_key] = LinkedList()
        
        self._buckets[hashed_key].insert([key, value])



    def get(self, key):
        """
        Given a key, return the value. If the key doesn't exist raise an error
        """
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]
        current = bucket.head

        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        
        raise KeyError(f"Key not found: {key}")


    def has(self):
        # method body here
        pass


    def keys(self):
        # method body here
        pass