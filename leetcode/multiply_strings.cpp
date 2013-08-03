#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>

using namespace std;

class Solution {
public:
  typedef string::const_reverse_iterator it_t;
  string
  add(const string& num1, const string& num2) {
    size_t num1Sz = num1.size(), num2Sz = num2.size();
    size_t longer = (num1Sz > num2Sz) ? num1Sz : num2Sz;
    bool borrow = false;
    string result;
    for (size_t i = 0; i != longer; ++i) {
      int val = 0;
      if (num1.size() > i) val += (num1[num1Sz - 1 - i] - '0');
      if (num2.size() > i) val += (num2[num2Sz - 1 - i] - '0');
      if (borrow) val++;
      if (val >= 10) {
        borrow = true;
        val -= 10;
      } else {
        borrow = false;
      }
      result.insert(result.begin(), '0' + val);
    }
    if (borrow) result.insert(result.begin(), '1');
    return result;
  }

  string
  multiply(const string& num, char c, int index) {
    int borrow = 0;
    string result("");
    for (it_t p = num.rbegin(); p != num.rend(); ++p) {
      char digit = *p;
      int val = (digit - '0') * (c - '0');
      val += borrow;
      borrow = val / 10; // reset borrow
      val %= 10; // reset val after deducing borrow
      result.insert(result.begin(), '0' + val);
    }
    if (borrow) result.insert(result.begin(), '0' + borrow);
    for (int i = 0; i < index; ++i) result.push_back('0');
    return result;
  }

  void
  rmStartingZeroes(string& s) {
    while (s.size() > 1 && s[0] == '0') {
      s.erase(0, 1);
    }
  }

  string
  multiply(string num1, string num2) {
    // Start typing your C/C++ solution below
    // DO NOT write int main() function
    string result("0");
    int szNum2 = num2.size();
    for (int i = szNum2 - 1; i >= 0; --i ) {
      //std::cout << i << ": " << result << endl;
      string s = multiply(num1, num2[i], szNum2 - 1 - i);
      result = add(result, s);
    }
    rmStartingZeroes(result);
    return result;
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::cout << argv[1] << " * " << argv[2] << " = " << std::endl;
  std::cout << s.multiply(argv[1], argv[2]) << std::endl;
}
