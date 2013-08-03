public class Solution {
    public int threeSumClosest(int[] num, int target) {
        int result = 0;
        int closest = Integer.MAX_VALUE;
        int len = num.length;
        Arrays.sort(num);

        for (int i = 0; i < len - 2; ++i) {
            int j = i + 1, k = len - 1;
            while (j < k) {
                int sum = num[i] + num[j] + num[k];
                if (Math.abs(sum - target) < closest) {
                    closest = Math.abs(sum - target);
                    result = sum;
                }
                if (sum > target) {
                    --k;
                } else if (sum < target) {
                    ++j;
                } else {
                    return result;
                }
            }
        }
        return result;
    }
}