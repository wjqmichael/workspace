/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  ListNode *
  removeNthFromEnd(ListNode *head, int n) {
    ListNode *nth = head, *prev = NULL, *iter = head;
    for (int i = 1; i < n; ++i)
      iter = iter->next;
    while (iter->next != NULL) {
      prev = nth;
      nth = nth->next;
      iter = iter->next;
    }

    if (prev) prev->next = nth->next;
    if (nth == head) return nth->next;
    return head;
  }
};
