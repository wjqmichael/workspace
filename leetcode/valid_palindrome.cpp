#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isAlphaNum(char c) {
        return isalnum(c);
    }
    bool isPalindrome(string s) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (!isAlphaNum(s[left])) ++left;
            else if (!isAlphaNum(s[right])) --right;
            else if (tolower(s[left++]) != tolower(s[right--])) return false;
        }
        return true;
    }
};

int main() {
  Solution s;
  cout << isalnum('.') << endl;
  cout << isalnum(',') << endl;
  cout << s.isPalindrome("a.b,.") << endl;
  return 0;
}
