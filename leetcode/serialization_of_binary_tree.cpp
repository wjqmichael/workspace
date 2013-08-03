#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include "bst.hpp"

using namespace std;

int main() {
  Tree t;
  t.insert(5);
  t.insert(2);
  t.insert(7);
  t.insert(0);
  t.insert(100);
  t.insert(95);
  ofstream ofs("test.txt");
  t.serialize(ofs);
  ofs.close();
  cout << t << endl;
  ifstream ifs("test.txt");
  Tree t2;
  t2.deserialize(ifs);
  cout << t2 << endl;
  return 0;
}
