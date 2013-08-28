from list import List, Node

def removeNthFromEnd(lst, n):
    cur = lst.head
    for x in xrange(n-1): cur = cur.next
    nth = lst.head
    n_1th = None
    while (cur != lst.tail):
        cur = cur.next
        n_1th = nth
        nth = nth.next
    n_1th.next = nth.next
    if nth == lst.tail:
        lst.tail = n_1th
    del nth

lst = List([1,2,3,4,5])
removeNthFromEnd(lst, 2)
print lst

