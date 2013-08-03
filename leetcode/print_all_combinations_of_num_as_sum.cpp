#include <iostream>
#include <vector>
#include <iterator>
#include <cstdlib>

using namespace std;

void printSum(const vector<int>& candidates, const vector<int>& index, int n) {
  for (int i = 1; i < n; ++i) {
    cout << candidates[index[i]] << (i==n-1?"\n":"+");
  }
}

void solve(int target, int sum, const vector<int>& candidates, vector<int>& index, int n) {
  if (sum > target) return;
  if (sum == target) {
    printSum(candidates, index, n);
    return;
  }
  for (int i = index[n - 1]; i < candidates.size(); ++i) {
    index[n] = i;
    solve(target, sum + candidates[i], candidates, index, n + 1);
  }
}

int main(int argc, char** argv) {
  int target = atoi(argv[1]);
  vector<int> candidates;
  vector<int> index;
  for (int i = 2; i < argc; ++i) {
    candidates.push_back(atoi(argv[i]));
  }

  index.assign(10000, 0);
  solve(target, 0, candidates, index, 1);
  return 0;
}
