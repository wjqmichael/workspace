# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if not root:
            return 0
        max_sum = [root.val]
        self.helper(root, max_sum)
        return max_sum[0]

    def helper(self, node, max_sum):
        if not node:
            return 0
        l_sum = self.helper(node.left, max_sum)
        r_sum = self.helper(node.right, max_sum)
        rt = max(node.val, node.val + l_sum, node.val + r_sum)
        max_sum[0] = max(max_sum[0], max(rt, node.val + l_sum + r_sum))
        return rt

