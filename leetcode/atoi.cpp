#include <cstdlib>
#include <climits>
#include <iostream>
#include <cctype>
using namespace std;

class Solution {
public:
  int
  atoi(const char *str) {
    bool sign = true;
    while (*str == ' ') ++str;
    if (*str == '-') {
      sign = false;
      ++str;
    } else if (*str == '+') ++str;

    int result = 0;
    bool overflow = false;
    for (; *str != '\0'; ++str) {
      if (!isdigit(*str)) break;
      int n = *str - '0';
      if ((INT_MAX - n)/10 < result) {
        overflow = true;
        break;
      }
      result = 10*result + n;
    }
    if (overflow) return sign ? INT_MAX : INT_MIN;
    return sign ? result : -result;
  }
};

int main(int argc, char** argv) {
  Solution s;
  //cout << s.atoi(argv[1]) << endl;
  cout << INT_MAX << endl;
  cout << INT_MIN << endl;
  return EXIT_SUCCESS;
}
