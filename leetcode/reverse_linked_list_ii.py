# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        
        prev, left = dummy, None
        for i in xrange(1, n + 1):
            if i <= m:
                if i == m: left = prev
                prev = prev.next
                head = head.next
            else:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
        left.next.next = head
        left.next = prev

        return dummy.next