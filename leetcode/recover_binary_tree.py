# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return '{0}, {1}, {2}'.format(self.val, self.left, self.right)

class Solution:
    # @param root, a tree node
    # @return a tree node

    # This solution use O(n) time and O(1) space
    def recoverTree(self, root):
        helper_list = [None, None, None]
        def helper(node, helper_list):
            if node is None: return
            helper(node.left, helper_list)
            prev, first, second = helper_list
            if prev is not None and prev.val > node.val:
                if first is None: 
                    helper_list[1] = prev
                helper_list[2] = node
            helper_list[0] = node
            helper(node.right, helper_list)
        helper(root, helper_list)
        prev, first, second = helper_list
        first.val, second.val = second.val, first.val
        return root
        
    # def recoverTree(self, root):
    #     prev, first, second = None, None, None
    #     def helper(node):
    #         if node is None: return
    #         helper(node.left)
    #         if prev is not None and prev.val > node.val:
    #             if first is None: 
    #                 first = prev
    #             else:
    #                 second = node
    #         prev = node
    #         helper(node.right)
    #     helper(root)
    #     first.val, second.val = second.val, first.val
    #     return root

    # This solution use O(nlogn) time and O(logn) space
    # def recoverTree(self, root):
    #     inorder_rt = []
    #     def inorder(node):
    #         if node is None: return
    #         inorder(node.left)
    #         inorder_rt.append(node)
    #         inorder(node.right)
    #     inorder(root)
    #     expected = [i.val for i in sorted(inorder_rt, key=lambda node: node.val)]
    #     for i, v in enumerate(expected):
    #         inorder_rt[i].val = v
    #     return root

root = TreeNode(0)
root.left = TreeNode(1)
print(root)

root = Solution().recoverTree(root)
print(root)

