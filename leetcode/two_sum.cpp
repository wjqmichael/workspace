class Solution {
  typedef vector<int>::const_iterator it_t;

public:
  vector<int>
  twoSum(vector<int> &numbers, int target) {
    // Start typing your C/C++ solution below
    // DO NOT write int main() function
    vector<int> sorted = numbers;
    sort(sorted.begin(), sorted.end());
    int s = 0, e = sorted.size() - 1;
    while (e > s && sorted[s] + sorted[e] != target) {
      if (sorted[s] + sorted[e] > target) --e;
      else ++s;
    }
    it_t first = find(numbers.begin(), numbers.end(), sorted[s]);
    it_t second = find(numbers.begin(), numbers.end(), sorted[e]);
    if (second == first) {
      second = find(++second, numbers.end(), sorted[e]);
    }
    int index1 = (first - numbers.begin()) + 1;
    int index2 = (second - numbers.begin()) + 1;

    vector<int> result;
    result.push_back(min(index1, index2));
    result.push_back(max(index1, index2));
    return result;
  }
};
