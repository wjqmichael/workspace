# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def list_len(self, head):
        rt = 0
        while head:
            rt += 1
            head = head.next
        return rt

    def helper(self, list_node, start, end):
        if start > end: return None
        mid = start + (end - start) / 2
        left_child = self.helper(list_node, start, mid - 1)
        tree_node = TreeNode(list_node[0].val)
        tree_node.left = left_child
        list_node[0] = list_node[0].next
        tree_node.right = self.helper(list_node, mid + 1, end)
        return tree_node

    def sortedListToBST(self, head):
        return self.helper([head], 0, self.list_len(head) - 1)

head = None
print Solution().list_len(head)
# print Solution().sortedListToBST(head)