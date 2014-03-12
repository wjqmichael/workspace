# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        def helper(node, current_sum):
            if not node: return False
            if not node.left and not node.right:
                return node.val == current_sum
            return helper(node.left, current_sum - node.val) or \
                helper(node.right, current_sum - node.val)

        if root is None: return False
        return helper(root, sum)