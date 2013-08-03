#include <cstddef>
#include <iostream>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) :
      val(x), next(NULL) {
  }
};

ostream& operator<<(ostream& out, ListNode* head) {
  while(head) {
    out << (head->val) << "->";
    head = head->next;
  }
  return out;
}

class Solution {
public:
  // Recursive solution
  ListNode *
  swapPairs(ListNode *head) {
    ListNode *ret = head && (head->next) ? (head->next) : head;
    if (head && head->next) {
      ListNode *second = head->next;
      head->next = swapPairs(second->next);
      second->next = head;
      head = head->next;
    }
    return ret;
  }

  // Iterative solution
  ListNode *
  swapPairs2(ListNode *head) {
    if (head == NULL || head->next == NULL) return head;
    ListNode *ret = head->next;
    ListNode *pre = NULL, *cur = head;
    while (cur) {
      ListNode *nxt = cur->next;
      if (pre) pre->next = nxt ? nxt : cur;
      pre = cur;
      if (nxt) {
        ListNode *tmp = nxt->next;
        nxt->next = cur;
        cur = tmp;
      } else cur = NULL;
    }
    if (pre) pre->next = NULL;
    return ret;
  }
};



int main() {
  ListNode l1(1), l2(2), l3(3), l4(4);
  l1.next = &l2;
  l2.next = &l3;
  l3.next = &l4;
  cout << &l1 << endl;
  Solution solution;
  ListNode* n = solution.swapPairs2(&l1);
  cout << n << endl;
  //cout << n;
}
