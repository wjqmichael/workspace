from my_list import Node, iter_to_node, node_to_iter

def rotateRight(head, k):
    assert(head)
    leng = 1
    tail = head
    while tail.next:
        leng += 1
        tail = tail.next

    if not k % leng:
        return head

    count = leng - (k % leng)
    prev = None
    rt = head
    while count:
        prev = rt
        rt = rt.next
        count -= 1
    tail.next = head
    prev.next = None
    return rt


for i in xrange(7):
    n = iter_to_node([1,2,3,4,5])
    print list(node_to_iter(rotateRight(n, i)))
