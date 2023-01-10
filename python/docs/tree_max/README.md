# Challenge Summary
Building upon our existing Binary Tree class, create a new method that will find the maximum value in a binary tree.

## Whiteboard Process
![find-max](/docs/tree_max/find_maximum_value.png)

## Approach & Efficiency
- Check if binary tree is empty, if yes, return None. If not, use the built-in max() method using the pre-order method to populate a binary tree with nodes. Return the max value.
- Big O: O(n) for both time and space, per Python docs. Each node will need to be compared, so the complexity will increase linearly with the size of the tree.
