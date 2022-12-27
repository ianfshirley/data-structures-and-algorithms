# Singly Linked List

## Challenge
- Create a Node class has properties for the value stored in the Node, and a pointer to the next Node.
- Create a LinkedList class with a 'head' property
  - Upon instantiation, an empty linked list should be created.
    - The class should contain the following methods:
      - insert
        - Arguments: value
        - Returns: nothing
        - Adds a new node with that value to the head of the list with an O(1) Time performance.
      - includes
        - Arguments: value
        - Returns: Boolean
        - Indicates whether that value exists as a Node’s value somewhere within the list.
        - to string
          - Arguments: none
          - Returns: a string representing all the values in the Linked List, formatted as:
            "{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency
- I made a Node class to create new nodes.
- I made a LinkedList class to instantiate a new linked list.
- I made an insert method to add a new node to the beginning of the list.
- I made an includes method to check if a value exists in any of the nodes in the list.
- I made a "to string" method to return all the values in the linked list as a string.
- I used while loops to traverse through the list(s) for the includes & to string methods, because it was the only way
  I could think to complete the required tasks.

## API
<!-- Description of each method publicly available to your Linked List -->
I don't know what this means
