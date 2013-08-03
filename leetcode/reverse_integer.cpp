class Solution {
public:
    int reverse(int x) {
      bool neg = false;
      if (x < 0) {
        neg = true;
        x = -x;
      }

      int result = 0;
      for (; x != 0; x /= 10) {
        int digit = x%10;
        result = 10*result + digit;
      }

      return (neg ? -result : result);
    }
};
