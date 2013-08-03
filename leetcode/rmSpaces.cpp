#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void rmSpaces(string& s) {
  for (string::iterator p = s.begin(); p != s.end(); ++p) {
//    if 
}

int main(int argc, char* argv[]) {
  string s("abcde fg    hij");
  rmSpaces(s);
  cout << s << endl;
  string s2("");
  rmSpaces(s2);
  cout << s2 << endl;
  string s3("abc");
  rmSpaces(s3);
  cout << s3 << endl;

  return 0;
}
