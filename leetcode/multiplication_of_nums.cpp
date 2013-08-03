#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

vector<int> multiplicationNum(vector<int>& input) {
  int sz = input.size();
  vector<int> output(sz, 1);
  int left = 1;
  int right = 1;
  for (int i = 0; i < sz; ++i) {
    output[i] *= left;
    output[sz - 1 - i] *= right;
    left *= input[i];
    right *= input[sz - 1 - i];
  }
  return output;
}

int main(int argc, char* argv[]) {
  int ia[] = {4, 3, 2, 1, 2};
  vector<int> input(ia, ia+sizeof(ia)/sizeof(int));
  vector<int> output = multiplicationNum(input);
  ostream_iterator<int> outIt(cout, " ");
  copy(output.begin(), output.end(), outIt);
  cout << endl;
  return 0;
}
