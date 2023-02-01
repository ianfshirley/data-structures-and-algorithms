from data_structures.binary_tree import BinaryTree


def tree_intersection(tree1, tree2):
    shared = {}
    def walk(node1, node2):
        if node1 is None or node2 is None:
            return
        if node1.value == node2.value:
            if node1.value not in shared:
                shared[node1.value] = 1
        walk(node1.left, node2.left)
        walk(node1.right, node2.right)
    walk(tree1.root, tree2.root)
    return list(shared.keys())