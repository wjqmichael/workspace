# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        def depth_helper(node, depth):
            if not node: 
                return depth
            return max(depth_helper(node.left, depth + 1), 
                depth_helper(node.right, depth + 1))
        return depth_helper(root, 0)