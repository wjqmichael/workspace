class Solution {
public:
  bool
  isPalindrome(int x) {
    if (x < 0) return false;
    int div = 1;
    while (x/div >= 10) div *= 10;
    while (x) {
      int high = x/div;
      int low = x%10;
      if (high != low) return false;
      x %= div;
      x /= 10;
      div /= 100;
    }
    return true;
  }
};
