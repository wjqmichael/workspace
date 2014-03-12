import java.lang.Math;

public class Solution {
    public boolean canJump(int[] A) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int reach = 0;
        int len = A.length;
        for (int i = 0; i <= reach && reach < len - 1; ++i) {
            reach = Math.max(reach, A[i] + i);
        }

        return reach >= len - 1;
    }
}