# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        while root and root.left:
            nxt_lvl = root.left
            root.left.next = root.right
            while root.next:
                root.right.next = root.next.left
                root = root.next
                root.left.next = root.right
            root = nxt_lvl