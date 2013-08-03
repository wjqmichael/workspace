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
  class Comparator {
  public:
    bool
    operator()(ListNode* left, ListNode* right) const {
      return (left->val > right->val);
    }
  };

  ListNode *
  mergeKLists(vector<ListNode *> &lists) {
    typedef vector<ListNode *>::iterator it_t;
    it_t p = lists.begin();
    while (p != lists.end()) {
      if (!*p) p = lists.erase(p);
      else ++p;
    }
    Comparator comp = Comparator();
    ListNode *head = NULL, *tail = NULL;
    make_heap(lists.begin(), lists.end(), comp);
    while (!lists.empty()) {
      if (!head) head = tail = lists[0];
      else tail = tail->next = lists[0];
      pop_heap(lists.begin(), lists.end(), comp);
      size_t sz = lists.size();
      if (lists[sz - 1]->next) {
        lists[sz - 1] = lists[sz - 1]->next;
        push_heap(lists.begin(), lists.end(), comp);
      } else lists.pop_back();
    }
    return head;
  }
};
