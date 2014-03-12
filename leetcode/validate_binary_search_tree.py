# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def helper(node, min_val, max_val):
            if node is None: return True
            if node.val > max_val or node.val < min_val: return False
            return helper(node.left, min_val, min(max_val, node.val)) and \
                helper(node.right, max(min_val, node.val), max_val)
        import sys
        return helper(root, -sys.maxint - 1, sys.maxint)


root = TreeNode(100)
root.left = TreeNode(101)
print Solution().isValidBST(root)