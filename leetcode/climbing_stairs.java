import java.lang.Math;

public class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        int dp1 = 1;
        int dp2 = 2;
        for (int i = 0; i < n - 2; ++i) {
            int s = dp1 + dp2;
            if (dp1 < dp2) dp1 = s;
            else dp2 = s;
        }
        return Math.max(dp1, dp2);
    }
}