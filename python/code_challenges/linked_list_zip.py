from data_structures.linked_list import LinkedList


def zip_lists(ll1, ll2):
    new_ll = LinkedList()
    while ll1.head or ll2.head:
        if ll1.head:
            new_ll.append(ll1.head.value)
            ll1.head = ll1.head.next
        if ll2.head:
            new_ll.append(ll2.head.value)
            ll2.head = ll2.head.next
    return new_ll

