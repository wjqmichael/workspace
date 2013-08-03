#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <boost/dynamic_bitset.hpp>
#include <iterator>

using namespace std;

vector<int> eratosthenesSieve(int n) {
  vector<int> result;
  if (n < 2) return result;
  boost::dynamic_bitset<> isPrime(n);
  isPrime.flip();
  for (int i = 2; i <= n; i++) {
    if (isPrime[i-1]) {
      result.push_back(i);
      int mark = i*i;
      while (mark <= n) {
        isPrime.reset(mark - 1);
        mark += i;
      }
    }
  }
  return result;
}

int main(int argc, char* argv[]) {
  vector<int> r = eratosthenesSieve(100);
  ostream_iterator<int> out(cout, " ");
  copy(r.begin(), r.end(), out);
  cout << endl;
  return 0;
}
