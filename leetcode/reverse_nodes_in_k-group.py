import my_list

def reverse_k_group(node, k):
    """
    recursive solution
    """
    k_nodes = []
    head = node
    for i in xrange(k):
        if node is None:
            return head
        k_nodes.append(node)
        node = node.next
    for i in xrange(len(k_nodes) - 1, 0, -1):
        k_nodes[i].next = k_nodes[i - 1]
    k_nodes[0].next = reverse_k_group(node, k)
    return k_nodes[-1]

def reverse_k_group_2(node, k):
    """
    Non-recursive solution
    Space complexity O(k)
    """
    head = node
    prev = None
    k_nodes = []
    while node is not None: 
        k_nodes.append(node)
        node = node.next
        if len(k_nodes) == k:
            for i in xrange(len(k_nodes) - 1, 0, -1):
                k_nodes[i].next = k_nodes[i - 1]
            if prev is not None:
                prev.next = k_nodes[k - 1]
            else:
                head = k_nodes[k - 1]
            prev = k_nodes[0]
            k_nodes = []
    if prev:
        prev.next = k_nodes[0] if len(k_nodes) > 0 else None
    return head

def reverse_k_group_3(node, k):
    """
    Non-recursive solution
    Space complexity O(constant)
    """
    def kth(node, k):
        for i in xrange(k - 1):
            if node is None:
                return node
            node = node.next
        return node

    def reverse(node, k):
        """
        Reverse the k nodes.
        Precondition: node has >k nodes left.

        Returns:
            (the first element, the kth element, the (k+1)th element)
        """
        cur = node
        prev = None
        for i in xrange(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return node, prev, nxt

    kth_node = kth(node, k)
    head = kth_node if kth_node is not None else node
    last_prev = None
    while kth(node, k) is not None:
        one, kth_node, node = reverse(node, k)
        if last_prev is not None:
            last_prev.next = kth_node
        last_prev = one
    if last_prev is not None:
        last_prev.next = node
    return head            
    
if __name__ == '__main__':
    n = my_list.iter_to_node([1,2,3,4,5])
    func = reverse_k_group_3
    assert(list(my_list.node_to_iter(func(n, 3))) == [3,2,1,4,5])
    n = my_list.iter_to_node([])
    assert(list(my_list.node_to_iter(func(n, 3))) == [])
    n = my_list.iter_to_node([1,2,3,4,5])
    assert(list(my_list.node_to_iter(func(n, 2))) == [2,1,4,3,5])
    n = my_list.iter_to_node([1,2,3,4,5])
    assert(list(my_list.node_to_iter(func(n, 1))) == [1,2,3,4,5])
    n = my_list.iter_to_node([1,2,3,4,5])
    assert(list(my_list.node_to_iter(func(n, 5))) == [5,4,3,2,1])
