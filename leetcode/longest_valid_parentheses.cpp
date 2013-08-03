#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
  template<typename FwdIt>
    bool
    helper(FwdIt first, FwdIt last, int& maxSoFar, char l = '(', bool oneRun =
        false) {
      int current = 0;
      int pCount = 0;
      for (; first != last; ++first) {
        ++current;
        if (*first == l) ++pCount;
        else { // ')'
          if (!pCount) {
            if (oneRun) return false;
            current = 0;
          }
          if (pCount > 0) {
            --pCount;
            if (!pCount && current > maxSoFar) maxSoFar = current;
          }
        }
      }
      return (current - pCount) > maxSoFar;
    }

  int
  longestValidParentheses(string s) {
    int maxSoFar = 0;
    if (helper(s.begin(), s.end(), maxSoFar)) {
      helper(s.rbegin(), s.rend(), maxSoFar, ')', true);
    }
    return maxSoFar;
  }
};

int
main() {
  Solution s;
  cout << s.longestValidParentheses("((()))())") << endl;
  return 0;
}
