#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
public:
  vector<vector<int> >
  combinationSum(vector<int> &candidates, int target) {
    // Start typing your C/C++ solution below
    // DO NOT write int main() function
    sort(candidates.begin(), candidates.end());
    vector<int> index;
    index.push_back(0);
    vector < vector<int> > result;
    helper(candidates, target, index, 0, result);
    return result;
  }

  void
  helper(const vector<int> &candidates, int sum, vector<int>& index, int indexL,
      vector<vector<int> >& result) {
    if (sum == 0) writeResult(result, candidates, index, indexL);
    else {
      indexL++;
      for (int i = index[indexL - 1]; i < candidates.size(); ++i) {
        int nxtSum = sum - candidates[i];
        if (nxtSum < 0) return;
        changeOrPush(index, indexL, i);
        helper(candidates, sum - candidates[i], index, indexL, result);
      }
    }
  }

  void
  changeOrPush(vector<int>& index, int indexL, int val) {
    if (index.size() < indexL + 1) {
      assert(index.size() == indexL);
      index.push_back(val);
    } else index[indexL] = val;
  }

  void
  writeResult(vector<vector<int> >& result, const vector<int> &candidates,
      const vector<int>& index, int indexL) {
    vector<int> r;
    for (int i = 1; i < indexL + 1; ++i) {
       r.push_back(candidates[index[i]]);
    }
    result.push_back(r);
  }

};

int main() {
  vector<int> candidates = {2, 3, 5};
  int target = 6;
  Solution s;
  vector<vector<int> > result = s.combinationSum(candidates, target);
  for (vector<int>& p1: result) {
    for (int& p2: p1) {
      cout << p2 << " ";
    }
    cout << endl;
  }
}
