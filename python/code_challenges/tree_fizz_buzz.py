from data_structures.kary_tree import KaryTree




def fizz_buzz_tree(tree):

    cloned = tree.clone()

    def fizz_buzz(node):
        if node.value % 5 == 0 and node.value % 3 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)

        for x in node.children:
            fizz_buzz(x)

        return node

    fizz_buzz(cloned.root)
    return cloned

