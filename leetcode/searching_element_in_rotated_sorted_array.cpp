#include <iostream>
#include <vector>

using namespace std;

int findElem(int elem, const vector<int>& array) {
  if (array.empty()) {
    return -1;
  }

  int left = 0;
  int right = array.size() - 1;
  
  while (left <= right) {
    int mid = left + (right - left)/2;
    if (array[mid] == elem) return mid;
    if (left == right) return -1;

    if (array[left] < array[mid]) {
      if (array[mid] < elem) left = mid + 1;
      else right = mid - 1;
    } else {
      if (array[mid] > elem) right = mid;
      else left = mid;
    }
  }
  return -1;
}

int main() {

}
