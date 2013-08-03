#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <iostream>
#include <cstdlib>

using namespace std;

class Solution {
public:
 
    bool verified(const vector<int>& trial) {
        int n = trial.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
              cout << i << " " << j << endl;
              cout << trial[i] << " " << trial[j] << endl;
                if (abs(trial[j] - trial[i]) == (j - i)) {
                  cout << "false" << endl;
                  return false;
                }
            }
        }
        cout << "true" << endl;            
        return true;
        
    }
    
    vector<string> toVecStr(const vector<int>& trial) {
        typedef vector<int>::const_iterator it_t;
        int n = trial.size();
        vector<string> result;
        for (it_t p = trial.begin(); p != trial.end(); ++p) {
            ostringstream oss;
            for (int i = 0; i < *p; ++i) oss << ".";
            oss << "Q";
            for (int i = 0; i < (n - 1 - *p); ++i) oss << ".";
            result.push_back(oss.str());
        }
        return result;
    }
    
    vector<vector<string> > solveNQueens(int n) {
        vector<vector<string> > result;
        vector<int> trial;
        for (int i = 0; i < n; ++i) trial.push_back(i);
        sort(trial.begin(), trial.end());

        do {
            if (verified(trial)) {
                result.push_back(toVecStr(trial));
            }
        } while (next_permutation(trial.begin(), trial.end()));
        return result;
    }

};

int main(int argc, char** argv) {
  Solution s;
  typedef vector<vector<string> > vec_x2_t;
  vec_x2_t result = s.solveNQueens(atoi(argv[1]));
  for (vec_x2_t::const_iterator p1 = result.begin(); p1 != result.end(); ++p1) {
    for (auto p2 = p1->begin(); p2 != p1->end(); ++p2) {
      std::cout << *p2 << std::endl;
    }
    std::cout << "---------" << std::endl;
  }
  return EXIT_SUCCESS;
}
