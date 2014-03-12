# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    rt = []
    current_list = []

    def helper(self, node, sum):
        if not node: return
        if not node.left and not node.right:
            if node.val == sum:
                self.rt.append(self.current_list + [node.val])
            return
        self.current_list.append(node.val)
        self.helper(node.left, sum - node.val)
        self.helper(node.right, sum - node.val)
        self.current_list.pop(-1)

    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.rt = []
        self.current_list = []
        self.helper(root, sum)
        return self.rt

root = TreeNode(1)
print Solution().pathSum(root, 0)