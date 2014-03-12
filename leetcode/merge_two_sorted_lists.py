from my_list import *

def mergeTwoLists(l1, l2):
    if not l1: 
        return l2
    if not l2:
        return l1
    if l1.data < l2.data:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


l1 = iter_to_node([1, 3, 5])
l2 = iter_to_node([7, 10, 15])
rt = mergeTwoLists(l1, l2)
print list(node_to_iter(rt))