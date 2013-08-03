#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>

using namespace std;

int wordCount(const string& s) {
  if (s.empty()) return 0;
  int count = 0;
  bool inWord = false;
  int i = 0;
  while (i < s.size()) {
    if (isalpha(s[i])) {
      if (!inWord) {
        count ++;
        inWord = true;
      }
    } else {
      inWord = false;
    }
    ++i;
  }
  return count;
}

int main(int argc, char* argv[]) {
  cout << wordCount("") << endl;
  cout << wordCount("  This is a game. Haha") << endl; 
  cout << wordCount("This   is a  game. Haha  ") << endl;
  return 0;
}
