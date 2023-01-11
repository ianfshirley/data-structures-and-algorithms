class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def post_order(self, root=None, nodes=None):
        """
        return a list of nodes in a BT, in post order
        """
        # Start at the root of our tree
        if root is None:
            root = self.root

        # First time method is invoked
        if nodes is None:
            nodes = []

        # Left child
        if root.left:
            self.post_order(root.left, nodes)
        # Right Child
        if root.right:
            self.post_order(root.right, nodes)
        # Root
        nodes.append(root.value)

        # print(f"the state of nodes is {nodes}")
        #Base Case
        return nodes


    def pre_order(self, root=None, nodes=None):
        """
        return a list of nodes in a BT, in pre order
        """
        # Start at the root of our tree
        if root is None:
            root = self.root

        # First time method is invoked
        if nodes is None:
            nodes = []

        # Root
        nodes.append(root.value)
        # Left child
        if root.left:
            self.pre_order(root.left, nodes)
        # Right Child
        if root.right:
            self.pre_order(root.right, nodes)

        # print(f"the state of nodes is {nodes}")
        # Base Case
        return nodes

    def in_order(self, root=None, nodes=None):
        """
        return a list of nodes in a BT, in in order
        """
        # Start at the root of our tree
        if root is None:
            root = self.root

        # First time method is invoked
        if nodes is None:
            nodes = []

        # Left child
        if root.left:
            self.in_order(root.left, nodes)
        # Root
        nodes.append(root.value)
        # Right Child
        if root.right:
            self.in_order(root.right, nodes)

        # print(f"the state of nodes is {nodes}")
        # Base Case
        return nodes

    def find_maximum_value(self):
        if self.root is None:
            return None
        return max(self.pre_order())