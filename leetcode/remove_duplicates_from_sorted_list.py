from my_list import *

def deleteDuplicates(head):
    if not head or not head.next: return head
    prev, cur = head, head.next
    while cur:
        if cur.data == prev.data: prev.next = cur.next
        else: prev = cur
        cur = cur.next
    return head


heads = [iter_to_node([1,1,1,2,2,3,4,5,5]), iter_to_node([1,1,1,2]), 
    iter_to_node([])]
for head in heads:
    print 'Original list: %r' % list(node_to_iter(head))
    rt = deleteDuplicates(head)
    print list(node_to_iter(rt))