#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;
typedef unsigned long ul_t;
void putlong(ul_t l) {
  char c = l%10 + '0';
  if (l/10 != 0) putlong(l/10);
  putchar(c);
}

int main(int argc, char* argv[]) {
  ul_t l = 0;
  cout << l << endl;
  putlong(l);
  cout << endl;
  return 0;
}
