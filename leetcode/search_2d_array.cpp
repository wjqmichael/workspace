#include <iostream>
#include <climits>
#include <vector>
#include <cstdlib>
using namespace std;

bool search(int val, const vector<vector<int> >& array) {
  int row = array.size();
  int col = array[0].size();
  int r = row - 1;
  int c = 0;
  while (r >= 0 && c <= col - 1) {
    cout << array[r][c] << endl;
    if (array[r][c] == val) {
      cout << "Found: r=" << r << " c=" << c << endl;
      return true;
    }
    if (val > array[r][c]) ++c;
    else --r;
  }
  return false;
}

int main(int argc, char** argv) {
  //construct 2d array
  vector<vector<int> > array;/*
  int a1[] = {1, 4, 7, 11, 15};
  int a2[] = {2, 5, 8, 12, 19};
  int a3[] = {3, 6, 9, 15, 22};
  int a4[] = {10, 13, 14, 17, 24};
  int a5[] = {18, 21, 23, 26, 30};*/
  
  int array_c[5][5] = {
    {1, 4, 7, 11, 15},
    {2, 5, 8, 12, 19},
    {3, 6, 9, 15, 22},
    {10, 13, 14, 17, 24},
    {18, 21, 23, 26, 30}
  };
  for (int i = 0; i < 5; ++i) {
    array.push_back(vector<int>(array_c[i], array_c[i]+(sizeof(array_c[i])/sizeof(int))));
  }
  cout << search(atoi(argv[1]), array) << endl;//sizeof(array)/sizeof(array[0]), sizeof(array[0])/sizeof(int)) << endl;
  return 0;
}
