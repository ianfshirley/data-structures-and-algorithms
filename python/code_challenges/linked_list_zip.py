from data_structures.linked_list import *


def zip_lists(a, b):
    a_current = a.head
    b_current = b.head
    if a.head is None:
        return b
    if b.head is None:
        return a
    while a_current and b_current:
        a_next = a_current.next
        b_next = b_current.next
        a_current.next = b_current
        if a_next:
            b_current.next = a_next
        a_current = a_next
        b_current = b_next
    return a






