class Solution {
public:
    int lengthOfLongestSubstring(string s) {
      int i = 0, curMax = 0, curStart = 0;
      vector<int> counting(26, 0);
      while (i < s.size()) {
        int index = s[i] - 'a';
        if (counting[index]) {
          curStart = s.find(s[i], curStart) + 1;
          counting.assign(26 ,0);
          i = curStart;
          index = s[i] - 'a';
        }
        counting[index] = 1;
        int curLen = i - curStart + 1;
        if (curLen > curMax) curMax = curLen;
        ++i;
      }
      return curMax;
    }
};
