#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

string excelRowNum(int i) {
  string result(1, (char)('a'+i%26));
  i /= 26;
  while (i > 0) {
    result = (char)('a' + (i-1)%26) + result;
    i = (i-1) / 26;
  }
  return result;
}

int main(int argc, char** argv) {
  cout << excelRowNum(atoi(argv[1])) << endl;
  return 0;
}
