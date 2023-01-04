from data_structures.queue import Queue


def multi_bracket_validation(str):

    # list of opening brackets
    o_lst = ["[", "{", "("]
    # list of closing brackets
    c_lst = ["]", "}", ")"]

    stack = []

    for i in str:
        if i in o_lst:
            stack.append(i)
        elif i in c_lst:
            # variable for position of i in closing list
            pos = c_lst.index(i)
            if ((len(stack) > 0) and
                    (o_lst[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

