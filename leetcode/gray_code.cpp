#include <iostream>
#include <vector>
#include <iterator>
#include <bitset>
#include <cmath>
#include <algorithm>

// Leetcode solution
class Solution {
public:
  vector<int>
  grayCode(int n) {
    vector<int> ret;
    ret.push_back(0);
    for (int i = 1; i <=n; ++i) {
      for (int j = ret.size() - 1; j >=0; --j) {
        ret.push_back(ret[j] | (1 << (i - 1)));
      }
    }
    return ret;
  }
};

// The recursive solution that is easier to read and understand
namespace mystd {

std::string
binaryStr(unsigned int i) {
  std::bitset < sizeof(i) * 8 > bs(i);
  return bs.to_string();
}

void
printBinary(unsigned int i) {
  std::cout << binaryStr(i) << std::endl;
}

std::vector<unsigned int>
greyCodeGen(unsigned int numBits) {
  if (numBits == 0) return {};
  if (numBits == 1) return {0, 1};
  std::vector<unsigned int> n_1 = greyCodeGen(numBits - 1);
  std::vector<unsigned int> n(n_1.begin(), n_1.end());
  const unsigned int highestBit = pow(2, numBits - 1);
  for (auto p = n_1.rbegin(); p != n_1.rend(); ++p) {
    n.push_back(highestBit + (*p));
  }
  return n;
}
}

int
main() {
  std::vector<unsigned int> v = mystd::greyCodeGen(4);
  for_each(v.begin(), v.end(), mystd::printBinary);
  return 0;
}
