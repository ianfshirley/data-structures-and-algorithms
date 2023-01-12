from data_structures.binary_tree import BinaryTree



def breadth_first(tree):
    staging = []
    result = []

    if tree.root is None:
        return []

    staging.append(tree.root)

    while len(staging) > 0:
        current = staging.pop(0)
        result.append(current.value)

        if current.left is not None:
            staging.append(current.left)
        if current.right is not None:
            staging.append(current.right)

    return result

