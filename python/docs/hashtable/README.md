# Hashtables

- Hashtables are a data structure that use key/value pairs. This means every Node or Bucket has both a key and a value.
- The basic idea of a hashtable is the ability to store the key into this data structure, and quickly retrieve the value. This is done through what we call a hash. A hash is the ability to encode the key that will eventually map to a specific location in the data structure that we can look at directly to retrieve the value.
- Since we are able to hash our key and determine the exact location where our value is stored, we can do a lookup in an O(1) time complexity.
- In any array, we could access the information of any element in the array if we already know the index, but usually we don't know the index and thus have to loop through each element in the array to find what we're looking for, which greatly decreases efficiency.
- Instead of adding elements to an array from beginning to end, a hash map uses a 'hash function' to place each item at a precise index location, based off its key.
- The hash function essentially takes a key and returns an integer. We use that integer to determine where the key/value pair should be placed in the array. The hash code is calculated in constant time and writing to an array at one index is O(1), so the hash map has O(1) access.
- The hash code is used again to read something from the hash map. Take the key, and run it through the hash code to get a number, and use that number to index the array. Calculating the hash code and reading an array at that index is all constant time, so the hash map has O(1) read access.

## Challenge

- Implement a Hashtable Class with the following methods:
  - set
    - Arguments: key, value
    - Returns: nothing
    - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    - Should a given key already exist, replace its value from the value argument given to this method.
  - get
    - Arguments: key
    - Returns: Value associated with that key in the table
  - has
    - Arguments: key
    - Returns: Boolean, indicating if the key exists in the table already.
  - keys
    - Returns: Collection of keys
  - hash
    - Arguments: key
    - Returns: Index in the collection for that key


## Approach & Efficiency
O(1)

## Link to Code
[hashtable.py](python/data_structures/hashtable.py)