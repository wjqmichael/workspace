#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
  // This is the char* version
  bool
  isMatch(const char *s, const char *p) {
    if (*s == '\0' && *p == '\0') return true;
    if (*p == '\0') return false;
    if (*(p + 1) != '*') {
      return charMatch(*s, *p) && isMatch(s + 1, p + 1);
    }
    return isMatch(s, p + 2) ||
        (charMatch(*s, *p) && isMatch(s+1, p));
  }

  // The following is the string version
  bool
  isMatch(const string& s, const string& p) {
    return helper(s, 0, p, 0);
  }

  bool
  helper(const string& s, int sInd, const string& p, int pInd) {
    if (pInd == p.size() && sInd == s.size()) return true;
    if (pInd == p.size()) return false;

    // pInd + 1 != '*'
    if (pInd + 1 > p.size() - 1 || p[pInd + 1] != '*') {
      return (sInd < s.size()) && charMatch(s[sInd], p[pInd]) && helper(s, sInd+1, p, pInd+1);
    }

    // pInd + 1 == '*'
    /*while (sInd < s.size() && charMatch(s[sInd], p[pInd])) {
      if (helper(s, sInd, p, pInd + 2)) return true;
      ++sInd;
    }*/
    return helper(s, sInd, p, pInd + 2) ||
        (sInd < s.size() && charMatch(s[sInd], p[pInd]) && helper(s, sInd + 1, p, pInd));
  }

  bool charMatch(char s, char p) {
    if (s == '\0' || p == '\0') return false;
    return (p == '.') ? true : (s == p);
  }
};

int main() {
  Solution solution;
  const char* s = "aa";
  const char* p = ".*c";
  cout << solution.isMatch(s, p) << endl;
}
