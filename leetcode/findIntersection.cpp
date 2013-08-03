#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

vector<int> findIntersection(const vector<int>& A, const vector<int>& B) {
  typedef vector<int>::const_iterator CI;
  CI itA = A.begin();
  CI itB = B.begin();
  vector<int> result;
  while (itA != A.end() && itB != B.end()) {
    if (*itA == *itB) {
      result.push_back(*itA);
      ++itA; ++itB;
    } else if (*itA < *itB) {
      ++itA;
    } else {
      ++itB;
    }
  }
  return result;
}

vector<int> findIntersection2(const vector<int>& A, const vector<int>& B) {
  typedef vector<int>::const_iterator CI;
  CI itA = A.begin();
  vector<int> result;
  while (itA != A.end()) {
    if (binary_search(B.begin(), B.end(), *itA)) result.push_back(*itA);
    ++itA;
  }
  return result;
}

int main(int argc, char* argv[]) {
  int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int b[] = {-1, 0, 2, 4, 5, 6, 11 };
  vector<int> A(a, a+sizeof(a)/sizeof(int));
  vector<int> B(b, b+sizeof(b)/sizeof(int));
  vector<int> result = findIntersection2(A, B);
  copy(result.begin(), result.end(), ostream_iterator<int>(cout, " "));
  return 0;
}
