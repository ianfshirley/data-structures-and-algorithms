# Stacks and Queues
- Stacks and Queues are data structures that consist of Nodes. Each Node references the next Node in the stack, but
does not reference its previous Node.
- Stacks:
  - follow the FILO / LIFO principles. The first Node added to the stack will be the last one removed. The last
    Node added will be the first one removed.
  - each stack recognizes a self.top Node
  - each Node's 'next' references the stack "below" it (pointing from top towards the bottom)
- Queues:
  - follow the FIFO / LILO principles. The first Node added to the queue will be the first one removed. The last Node
  added to the queue will be the last one removed.
  - each queue recognizes a self.front & a self.rear Node
  - each Node's 'next' references the stack "behind" it (pointing from front towards the rear)

## Challenge
- Create a Node class
- Create a Stack class with the following methods:
  - push
  - pop
  - peek
  - is_empty
- Create a Queue class with the following methods:
  - enqueue
  - dequeue
  - peek
  - is_empty

## API
- Stack class methods:
  - push
    - Arguments: value
    - adds a new node with that value to the top of the stack with an O(1) Time performance.
  - pop
    - Arguments: none
    - Returns: the value from node from the top of the stack
    - Removes the node from the top of the stack
    - Should raise exception when called on empty stack
  - peek
    - Arguments: none
    - Returns: Value of the node located at the top of the stack
    - Should raise exception when called on empty stack
  - is_empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the stack is empty
- Queue class methods:
  - enqueue
    - Arguments: value
    - adds a new node with that value to the back of the queue with an O(1) Time performance.
  - dequeue
    - Arguments: none
    - Returns: the value from node from the front of the queue
    - Removes the node from the front of the queue
    - Should raise exception when called on empty queue
  - peek
    - Arguments: none
    - Returns: Value of the node located at the front of the queue
    - Should raise exception when called on empty queue
  - is_empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the queue is empty

## Code
- [Stack](/data_structures/stack.py)
- [Queue](/data_structures/queue.py)
