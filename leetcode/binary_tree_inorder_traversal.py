# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        rt = []
        def helper(node):
            if not node: return
            if node.left: helper(node.left)
            rt.append(node.val)
            if node.right: helper(node.right)
        helper(root)
        return rt

