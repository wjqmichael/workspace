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
        while root:
            nxt_lv, current = None, None
            while root:
                for node in (root.left, root.right):
                    if node:
                        if not nxt_lv:
                            nxt_lv = node
                        if current:
                            current.next = node    
                        current = node
                root = root.next
            root = nxt_lv