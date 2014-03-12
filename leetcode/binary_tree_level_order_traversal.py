# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None: return []
        pending_q = [root]
        rt = []
        while pending_q:
            rt_lv, tmp_q = [], []
            for node in pending_q:
                rt_lv.append(node.val)
                if node.left: tmp_q.append(node.left)
                if node.right: tmp_q.append(node.right)
            rt.append(rt_lv)
            pending_q = tmp_q
        return rt
