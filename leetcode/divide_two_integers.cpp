class Solution {
public:
  int
  divide(int dividend, int divisor) {
    bool neg_dividend = dividend < 0;
    bool neg_divisor = divisor < 0;

    unsigned int u_dividend;
    unsigned int u_divisor;

    if (dividend < 0) {
      u_dividend = (unsigned int) (dividend ^ -1) + 1;
    } else u_dividend = dividend;

    if (divisor < 0) {
      u_divisor = (unsigned int) (divisor ^ -1) + 1;
    } else u_divisor = divisor;

    int result = mydiv(u_dividend, u_divisor);

    if (neg_dividend ^ neg_divisor) result = (result ^ -1) + 1;

    return result;
  }

  unsigned int
  mydiv(unsigned int dividend, unsigned int divisor) {
    if (dividend < divisor) return 0;
    if (dividend == divisor) return 1;

    int bit_count = 0;
    int num = divisor;

    if ((num << 1) > num) {
      num = divisor << 1;

      while (dividend > num) {
        bit_count++;

        if ((num << 1) > num) num <<= 1;
        else break;
      }

      return mydiv(dividend - (divisor << bit_count), divisor)
          + (1 << bit_count);
    } else return mydiv(dividend - divisor, divisor) + 1;
  }
};

