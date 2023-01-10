from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        """
        following the rules of a binary search tree, this method adds a new node at the correct location within the binary tree
        """
        if self.root is None:
            self.root = Node(value)
            return
        
        # start pointer at root
        current = self.root

        while current:
            # if number of the added node is less than the current node, check left
            if value < current.value:
                # add node only if there's space
                if current.left is None:
                    current.left = Node(value)
                    return
                # if there is no space, go left again
                current = current.left
            # if number of added node is greater than current node, check right
            else:
                # add node only if there's space
                if current.right is None:
                    current.right = Node(value)
                    return
                # if there's no space, go right again
                current = current.right


    def contains(self, value):
        """
        checks if a binary search tree contains a node with a specified value
        """
        if self.root is None:
            return False
        if self.root.value == value:
            return True
        if self.root.value > value:
            self.root = self.root.left
            return self.contains(value)
        if self.root.value < value:
            self.root = self.root.right
            return self.contains(value)
        
