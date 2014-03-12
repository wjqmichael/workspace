#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

string addBinary(string a, string b) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int numBits = max(a.size(), b.size());
        bool carry = false;
        int aVal, bVal;
        string result;
        char nxt;
        for (int i = 0; i < numBits; ++i) {
            if (a.size() > i) {
                aVal = a[a.size() - 1 - i] - '0';
            } else {
                aVal = 0;
            }
            if (b.size() > i) {
                bVal = b[b.size() - 1 - i] - '0';
            } else {
                bVal = 0;
            }
            int sum = aVal + bVal + (carry ? 1 : 0);
            carry = (sum>=2)?true:false;
            nxt = (sum%2)?'1':'0';
            result.insert(0, 1 ,nxt);
        }
        if (carry) result.insert(0, 1, '1');
        return result;
    }

int main() {
  cout << addBinary("100", "1111") << endl;
  return 0;
}
