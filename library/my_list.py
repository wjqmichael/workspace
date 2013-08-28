import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

def node_to_iter(node):
    while not node is None:
        yield str(node)
        node = node.next

def iter_to_node(iter):
    pre = None
    head = None
    for i in iter:
        cur = Node(i)
        if pre is None:
            head = cur
        else:
            pre.next = cur
        pre = cur
    return head

if __name__ == '__main__':
    n = iter_to_node([1,3,45,6,7])
    print list(node_to_iter(n))