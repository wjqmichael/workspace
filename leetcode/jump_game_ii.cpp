#include <utility>
#include <unordered_map>
#include <climits>


class Solution {
public:
    int jump(int A[], int n) {
        std::vector<int> leastJump(n, -1);
        leastJump[n-1] = 0;
        for (int i = n - 2; i >=0; --i) {
            int distToDest = (n - 1) - i;
            if (A[i] >= distToDest) leastJump[i] = 1;
            else {
                int least = INT_MAX;
                for (int relay = i + 1; relay <= i + A[i]; ++relay) {
                    if (leastJump[relay] != -1 && leastJump[relay] < least) {
                        least = leastJump[relay];
                    }
                }
                if (least != INT_MAX) leastJump[i] = least + 1;
            }
        }
        return leastJump[0];
        
    }
};
int main() {
  
  return EXIT_SUCCESS;
}
