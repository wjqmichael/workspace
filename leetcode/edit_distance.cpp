#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
      int sz1 = word1.size(), sz2 = word2.size();
      if (sz1 == 0) return sz2;
      if (sz2 == 0) return sz1;
      vector<vector<int> > minDist(sz1 + 1, vector<int>(sz2 + 1, 0));
      int sum = sz1 + sz2;
      for (int s = 1; s <= sum; ++s) {
        for (int i1 = 0; i1 <= sz1 && i1 <= s; ++i1) {
          int i2 = s - i1;
          if (i2 > sz2) continue;
          int val = 0;
          if (i1 == 0) val = i2;
          else if (i2 == 0) val = i1;
          else {
            val = minDist[i1 - 1][i2 - 1];
            if (word1[i1 - 1] != word2[i2 - 1]) ++val;
            val = min(val, 1 + minDist[i1 - 1][i2]);
            val = min(val, 1 + minDist[i1][i2 - 1]);
          }
          minDist[i1][i2] = val;
        }
      }
      return minDist[sz1][sz2];
    }
};

int main(int argc, char** argv) {
  Solution s;
  cout << s.minDistance(argv[1], argv[2]) << endl;
  return 0;
}
