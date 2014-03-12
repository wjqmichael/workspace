import java.lang.*;

public class min_path_sum {
    public int minPathSum(int[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) return 0;
        int row = grid.length;
        int col = grid[0].length;
        int[] dp = new int[col];
        for (int i = 0; i < col; ++i) {
            dp[i] = grid[0][i];
        }

        for (int r = 1; r < row; ++r) {
            dp[0] += grid[r][0];
            for (int c = 1; c < col; ++c) {
                dp[c] = Math.min(dp[c - 1], dp[c]) + grid[r][c];
            }
        }

        return dp[col - 1];
    }

    public static void main(String[] args) {
        System.out.println("hello world");
    }
}