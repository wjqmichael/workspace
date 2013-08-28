import my_list

# Recursive solution
def swap_pairs_recur(head):
    def helper(node):
        if node is None: return None
        if node.next is None: return node
        third = node.next.next
        second = node.next
        second.next = node
        node.next = helper(third)
        return second
    return helper(head)

# Cheating by swappping the values only :)
def swap_pairs_cheat(head):
    odd = False
    prev, node = None, head
    while not node is None:
        if odd: node.data, prev.data = prev.data, node.data
        odd = not odd
        prev = node
        node = node.next
    return head

def swap_pairs_non_recur(head):
    prev, new_head, current = None, None, head

    # Process each pair per loop
    while current:
        second = current.next
        if prev: prev.next = second if second else current
        else: new_head = second if second else current
        if not second: prev, current = None, None # Mark the end of loop
        else:
            next_current = second.next
            second.next, prev = current, current
            current = next_current
    if prev: prev.next = None

    return new_head

func = swap_pairs_non_recur

lst = [my_list.iter_to_node(i) for i in ([], [1], [1,2,3,4], [1,2,3,4,5])]

# hd = swap_pairs_recur(lst)
for node in lst:
    hd = func(node)
    print list(my_list.node_to_iter(hd))