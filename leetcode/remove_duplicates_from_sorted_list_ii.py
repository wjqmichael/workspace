from my_list import *

def deleteDuplicates(head):
    '''
    Non-recursive solution.
    '''

    # Set up head
    nh, tail = None, None
    lo, hi = head, head
    while hi:
        while hi.next and hi.next.data == hi.data: 
            hi = hi.next
        if lo == hi:
            if not nh:
                nh, tail = lo, lo
            else:
                tail.next = lo
                tail = lo
        lo, hi = hi.next, hi.next
    if tail: tail.next = None
    return nh

def deleteDuplicates2(head):
    '''
    Recursive solution.
    '''

    if not head or not head.next: return head
    p = head.next
    if p.data == head.data:
        while p.next and p.next.data == p.data: p = p.next
        return deleteDuplicates2(p.next)
    else:
        head.next = deleteDuplicates2(p)
    return head


deleteDuplicates = deleteDuplicates2
heads = [iter_to_node([1,2,3,3,4,4,5]), iter_to_node([1,1,1,2,3]), 
    iter_to_node([1,1,1]), iter_to_node([])]
for head in heads:
    print 'Original list: %r' % list(node_to_iter(head))
    rt = deleteDuplicates(head)
    print list(node_to_iter(rt))