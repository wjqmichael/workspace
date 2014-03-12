from math import log, ceil, pow

class SumSegmentTree(object):
    '''
    Segment tree for calculating the sum of arrays with random start index
    and end index.
    '''

    def __init__(self, arr):
        assert(arr)
        self.arr = arr
        height = int(ceil(log(len(arr), 2)) + 1)
        max_len = int(pow(2, height) - 1)
        self.seg_tree = [None] * max_len
        self.construct_seg_tree(0, 0, len(arr) - 1)

    def get_mid(self, start, end):
        return start + (end - start)/2

    @staticmethod
    def left_child(parent):
        return 2 * parent + 1

    @staticmethod
    def right_child(parent):
        return 2 * parent + 2

    def construct_seg_tree(self, node, start, end):
        if start == end:
            self.seg_tree[node] = self.arr[start]
        else:
            mid = self.get_mid(start, end)
            self.seg_tree[node] = self.construct_seg_tree(
                self.left_child(node), start, mid) + self.construct_seg_tree(
                self.right_child(node), mid + 1, end)
        return self.seg_tree[node]

    def get_sum(self, start, end):
        def helper(node, node_s, node_e):
            '''
            node_s & node_e, the array start and end index contained in the node
            ind. It's different from the arguments passed into get_sum
            '''
            if start > node_e or end < node_s:
                return 0
            if start <= node_s <= node_e <= end:
                return self.seg_tree[node]
            mid = self.get_mid(node_s, node_e)
            return helper(self.left_child(node), node_s, mid) + helper(
                self.right_child(node), mid + 1, node_e)

        return helper(0, 0, len(self.arr) - 1)

    def update_arr(self, ind, val):
        diff = val - self.arr[ind]
        self.arr[ind] = val
        self.update_tree(0, 0, len(self.arr) - 1, ind, diff)

    def update_tree(self, node, node_s, node_e, ind, diff):
        if ind > node_e or ind < node_s: 
            return
        self.seg_tree[node] += diff
        if node_s == node_e:
            return
        mid = self.get_mid(node_s, node_e)
        self.update_tree(self.left_child(node), node_s, mid, ind, diff)
        self.update_tree(self.right_child(node), mid + 1, node_e, ind, diff)


if __name__ == '__main__':
    tree = SumSegmentTree([1, 3, 5, 7, 9, 11])
    print 'Seg Tree: ', tree.seg_tree
    assert(tree.get_sum(0, 5) == 36)
    assert(tree.get_sum(0, 4) == 25)
    assert(tree.get_sum(0, 3) == 16)
    assert(tree.get_sum(0, 2) == 9)
    assert(tree.get_sum(0, 1) == 4)
    assert(tree.get_sum(0, 0) == 1)
    assert(tree.get_sum(1, 5) == 35)
    assert(tree.get_sum(1, 4) == 24)
    assert(tree.get_sum(1, 3) == 15)

    tree.update_arr(4, 0)
    # Now array becomes [1, 3, 5, 7, 0, 11]
    print 'Seg Tree: ', tree.seg_tree
    assert(tree.get_sum(0, 5) == 27)
    assert(tree.get_sum(0, 4) == 16)
    assert(tree.get_sum(0, 3) == 16)
    assert(tree.get_sum(0, 2) == 9)
    assert(tree.get_sum(0, 1) == 4)
    assert(tree.get_sum(0, 0) == 1)
    assert(tree.get_sum(1, 5) == 26)
    assert(tree.get_sum(1, 4) == 15)
    assert(tree.get_sum(1, 3) == 15)
