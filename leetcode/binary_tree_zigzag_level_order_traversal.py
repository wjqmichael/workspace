# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        current_lv, next_lv, rt = [root], [], []
        left_to_right = True
        while current_lv: 
            rt_lv = []
            for node in current_lv:
                rt_lv.append(node.val)
                if left_to_right:
                    if node.left: 
                        next_lv.append(node.left)
                    if node.right:
                        next_lv.append(node.right)
                else:
                    if node.right:
                        next_lv.append(node.right)
                    if node.left:
                        next_lv.append(node.left)
            rt.append(rt_lv)
            current_lv, next_lv = next_lv, []
            left_to_right = not left_to_right
        return rt