#include <cstddef>
#include <iostream>
#include <cassert>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) :
      val(x), next(NULL) {
  }
};

ostream&
operator<<(ostream& out, ListNode* head) {
  while (head) {
    out << (head->val) << "->";
    head = head->next;
  }
  return out;
}

class Solution {
public:
  bool
  hasKNodesLeft(ListNode* node, int k) {
    assert(k > 0);
    for (int i = 0; i < k; ++i) {
      if (!node) return false;
      node = node->next;
    }
    return true;
  }

  ListNode*
  getKthNode(ListNode* node, int k) {
    for (int i = 0; i < k; ++i) {
      if (!node) return NULL;
      node = node->next;
    }
    return node;
  }

  // This is the recursive solution (easy to code but takes more memory)
  ListNode*
  reverseKGroup(ListNode *head, int k) {
    if (!hasKNodesLeft(head, k)) return head;
    ListNode *prev = reverseKGroup(getKthNode(head, k), k);
    ListNode *cur = head, *nxt = head->next;
    for (int i = 0; i < k; ++i) {
      cur->next = prev;
      prev = cur;
      cur = nxt;
      if (nxt) nxt = nxt->next;
    }
    return prev;
  }

  // Non-recursive solution
  ListNode*
  reverseKGroup2(ListNode *head, int k) {
    ListNode *prevInK = NULL, *cur = head;
    if (!hasKNodesLeft(head, k)) return head;
    head = getKthNode(head, k - 1);
    while (hasKNodesLeft(cur, k)) {
      ListNode *nxtPrevInK = cur, *prev = NULL, *nxt = cur->next;
      for (int i = 0; i < k; ++i) {
        cur->next = prev;
        prev = cur;
        cur = nxt;
        if (nxt) nxt = nxt->next;
      }
      if (prevInK) prevInK->next = prev;
      prevInK = nxtPrevInK;
    }
    if (prevInK) prevInK->next = cur;
    return head;
  }
};

int
main() {
  ListNode l1(1), l2(2), l3(3), l4(4);
  l1.next = &l2;
  l2.next = &l3;
  /*l3.next = &l4;*/
  cout << &l1 << endl;
  Solution solution;
  ListNode* n = solution.reverseKGroup2(&l1, 1);
  cout << n << endl;
  //cout << n;
}
