class Solution {
public:
  typedef string::iterator it_t;

  bool
  noneIsEnd(const vector<it_t>& its, const vector<string> &strs) {
    for (int i = 0; i < its.size(); ++i) {
      if (its[i] == strs[i].end()) return false;
    }
    return true;
  }

  string
  longestCommonPrefix(vector<string> &strs) {
    string result;
    if (strs.empty()) return result;

    vector<it_t> its(strs.size());
    for (int i = 0; i < strs.size(); ++i) {
      its[i] = strs[i].begin();
    }
    while (noneIsEnd(its, strs)) {
      char c = *(its[0]);
      for (int i = 1; i != its.size(); ++i) {
        if (*(its[i]) != c) return result;
      }
      result.push_back(c);
      for (int i = 0; i != its.size(); ++i) ++its[i];
    }
    return result;
  }
};
