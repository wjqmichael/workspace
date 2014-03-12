from math import log, ceil, pow

class MinSegTree(object):
    def __init__(self, lst):
        self.lst = lst
        height = int(ceil(log(len(lst), 2))) + 1
        sz = int(pow(2, height) - 1)
        self.seg_tree = [None] * sz
        self.build_tree(0, len(lst) - 1, 0)
    
    @staticmethod
    def left_child(parent):
        return parent * 2 + 1

    @staticmethod
    def right_child(parent):
        return parent * 2 + 2

    @staticmethod
    def get_mid(start, end):
        return start + (end - start) / 2

    def build_tree(self, start, end, node):
        if start == end:
            self.seg_tree[node] = start
        else:
            mid = self.get_mid(start, end)
            l = self.build_tree(start, mid, self.left_child(node))
            r = self.build_tree(mid + 1, end, self.right_child(node))
            self.seg_tree[node] = l if self.lst[l] < self.lst[r] else r
        return self.seg_tree[node]

    def search(self, start, end):
        '''
        Attn: returned value is the node, not 
        '''
        def helper(node, node_s, node_e):
            if node_s > end or node_e < start:
                return None
            if start <= node_s <= node_e <= end:
                return self.seg_tree[node]
            mid = self.get_mid(node_s, node_e)
            l = helper(self.left_child(node), node_s, mid)
            r = helper(self.right_child(node), mid + 1, node_e)
            if l is None: return r
            if r is None: return l
            return l if self.lst[l] < self.lst[r] else r
        return helper(0, 0, len(self.lst) - 1)

def largestRectangleArea(heights):
    def helper(start, end, seg_tree):
        if start > end or start >= len(heights) or end < 0:
            return -1 
        lo = seg_tree.search(start, end)
        return max(
            heights[lo] * (end - start + 1),
            helper(start, lo - 1, seg_tree), 
            helper(lo + 1, end, seg_tree)
            )

    if not len(heights): return 0
    seg_tree = MinSegTree(heights)
    return helper(0, len(heights) - 1, seg_tree)
    
def largestRectangleArea2(heights):
    '''
    TODO: There is a O(n) solution on Geeks for Geeks.
    '''
    pass

def seg_tree_test():
    heights = [6, 2, 5, 4, 5, 3, 6]
    seg_tree = MinSegTree(heights)
    assert(seg_tree.search(0, 1) == 1)
    assert(seg_tree.search(0, 2) == 1)
    assert(seg_tree.search(0, 3) == 1)
    assert(seg_tree.search(0, 4) == 1)
    assert(seg_tree.search(0, 5) == 1)
    assert(seg_tree.search(0, 6) == 1)
    assert(seg_tree.search(2, 2) == 2)
    assert(seg_tree.search(2, 3) == 3)
    assert(seg_tree.search(2, 5) == 5)
    assert(seg_tree.search(2, 6) == 5)


seg_tree_test()
print largestRectangleArea([1])
print largestRectangleArea([2,1,5,6,2,3])
print largestRectangleArea([2,2,2,2,2,3])
print largestRectangleArea([1,2,3,4,5])
print largestRectangleArea([5,4,3,2,1])
print largestRectangleArea([6, 2, 5, 4, 5, 2, 6])
assert(largestRectangleArea([6, 2, 5, 4, 5, 2, 6]) == 14)
assert(largestRectangleArea([2,1,5,6,2,3]) == 10)