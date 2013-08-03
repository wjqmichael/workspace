#include <string>
#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

void reverseStr(string& s, int begin, int end) {
  for (int i = 0; i <= (end - begin)/2; ++i) {
    int left = begin + i;
    int right = end - i;
    char tmp = s[left];
    s[left] = s[right];
    s[right] = tmp;
  }
}

void rotate(string& s, int k) {
  int n = s.size();
  reverseStr(s, 0, n-1);
  reverseStr(s, 0, k-1);
  reverseStr(s, k, n-1);
}

int main() {
  string s("abcdefg");
  cout << s << endl;
  rotate(s, 3);
  cout << s << endl;
  return 0;
}

