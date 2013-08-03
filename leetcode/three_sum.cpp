//http://www.leetcode.com/2010/04/finding-all-unique-triplets-that-sums.html

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <iterator>

using namespace std;
typedef typename std::set<std::vector<int> > set_t;

class Solution {
public:
  vector<vector<int> >
  threeSum(vector<int> &num) {
    sort(num.begin(), num.end());

  }
};

set_t
threeSum(vector<int>& input) {
  sort(input.begin(), input.end());
  set_t result;
  int n = input.size();
  for (int i = 0; i != n; ++i) {
    int val1 = input[i];
    int j = i + 1;
    int k = n - 1;
    while (k > j) {
      if (input[j] + input[k] > -val1) {
        --k;
      } else if (input[j] + input[k] < -val1) {
        ++j;
      } else {
        vector<int> tmp = { input[i], input[j], input[k] };
        result.insert(tmp);
        ++j;
        --k;
      }
    }
  }
  return result;
}

int
main() {
  int input[] = { -1, 0, 1, 2, -1, -4 };
  vector<int> iv(input, input + sizeof(input) / sizeof(int));
  set < vector<int> > s = threeSum(iv);
  ostream_iterator<int> out_it(cout, " ");
  for (auto p = s.begin(); p != s.end(); ++p) {
    copy(p->begin(), p->end(), out_it);
    cout << endl;
  }
  return 0;
}
