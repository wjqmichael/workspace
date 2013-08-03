#include <bitset>
#include <string>
#include <iostream>
using namespace std;

int num_1_count_brute_force(const string& s) {
  static const int SZ = 100;
  bitset<SZ> bs(s);
  cout << bs.count() << endl;
  unsigned long input = bs.to_ulong();
  int count = 0;
  while (input > 0) {
    if ((input & 1) > 0) ++count;
    input = input >> 1;
  }
  return count;
}

int num_1_count(const string& s) {
  static const int SZ = 100;
  bitset<SZ> bs(s);
  cout << bs.count() << endl;
  unsigned long input = bs.to_ulong();
  int count = 0;
  while (input > 0) {
    input = input & (input - 1);
    count ++;
  }
  return count;
}


int main() {
  cout << num_1_count_brute_force("1001001110011") << endl;
  return 0;
}

