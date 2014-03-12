from my_list import *

def partition(head, x):
    lo_s, lo_e, hi_s, hi_e = None, None, None, None
    while head:
        if head.val >= x:
            if not hi_s: hi_s = head
            if hi_e: hi_e.next = head
            hi_e = head
        else:
            if not lo_s: lo_s = head
            if lo_e: lo_e.next = head
            lo_e = head
        head = head.next
    if lo_e: lo_e.next = hi_s
    else: lo_s = hi_s
    if hi_e: hi_e.next = None
    elif lo_e: lo_e.next = None
    return lo_s

head = iter_to_node([1, 4, 3, 2, 5, 2])
print list(node_to_iter(partition(head, 3)))