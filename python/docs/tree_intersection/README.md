# Challenge Summary
## Binary Tree Intersection (Find Common Values Between 2 Binary Trees)

- Write a function that takes in two binary trees as parameters, and return the values that are present in both trees.

- **Input**: 2 Binary Trees
- **Output**: A list of values that are present in both trees.

- **Edge Cases**:
  - If one or both lists are empty, return None
  - If there are no common values between the two trees, return None

## Whiteboard Process
![tree-intersection](python/docs/tree_intersection/tree-intersection.png)

## Approach & Efficiency
- Main function takes in 2 binary trees as arguments
- Create empty dict for shared values
- create recursive helper function to traverse and check for common values, and add to dict if present
- call helper function on root node of each tree
return list of dict's keys

- Big O:
  - Time: O(n) - Each node is visited once. Time will increase linearly with the number of nodes
  - Space: O(n) - Worst case is every node is in both trees, so every node may need to be saved to the dict

## Link to Code
[tree_intersection.py](python/code_challenges/tree_intersection.py)