# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        def helper(left, right):
            if left is None or right is None:
                return left is None and right is None
            return left.val == right.val and helper(left.left, right.right) \
                and helper(left.right, right.left)
        if root is None: 
            return True
        return helper(root.left, root.right)

# The following is the iterative solution
class Solution2:
    def isSymmetric(self, root):
        if root is None: 
            return True
        left_lst = [root.left]
        right_lst = [root.right]
        while left_lst and right_lst:
            node_l, node_r = left_lst.pop(0), right_lst.pop(0)
            if node_l is None and node_r is None:
                continue
            if node_l is None or node_r is None:
                return False
            if node_l.val != node_r.val: 
                return False
            left_lst.extend([node_l.left, node_l.right])
            right_lst.extend([node_r.right, node_r.left])
        return not left_lst and not right_lst
