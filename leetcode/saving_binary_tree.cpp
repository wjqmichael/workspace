#include "bst.hpp"
#include <fstream>

int main() {
  Tree t;
  t.insert(5);
  t.insert(2);
  t.insert(7);
  t.insert(0);
  t.insert(100);
  t.insert(95);
  //cout << t << endl;
  ofstream outFile("test.txt");
  t.preorder(outFile);
  outFile.close();
  ifstream inFile("test.txt");
  Tree t2;
  t2.read(inFile);
  cout << t2 << endl;
}
