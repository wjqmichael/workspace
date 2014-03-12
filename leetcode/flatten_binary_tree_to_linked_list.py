# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        while root:
            left, right = root.left, root.right
            root.left, root.right = None, left
            right_most = root
            while right_most.right:
                right_most = right_most.right
            right_most.right = right
            root = root.right
