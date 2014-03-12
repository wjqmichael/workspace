public class unique_paths_ii {
    public void initDp(int[][] dp, int[][] obstacleGrid) {
        int row = obstacleGrid.length;
        int col = obstacleGrid[0].length;

        int r = row - 1;
        while (r >= 0 && obstacleGrid[r][col - 1] == 0) {
            dp[r][col - 1] = 1;
            r -= 1;
        }

        while (r >= 0) {
            dp[r][col - 1] = 0;
            r -= 1;
        }   

        int c = col - 1;
        while (c >= 0 && obstacleGrid[row - 1][c] == 0) {
            dp[row - 1][c] = 1;
            c -= 1;
        }
        while (c >= 0) {
            dp[row - 1][c] = 0;
            c -= 1;
        }
    }

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid.length == 0 || obstacleGrid[0].length == 0) return 0;
        int row = obstacleGrid.length;
        int col = obstacleGrid[0].length;
        // if (obstacleGrid[row - 1][col - 1] == 1) return 0;

        int[][] dp = new int[row][col];
        initDp(dp, obstacleGrid);

        for (int r = row - 2; r >= 0; --r) {
            for (int c = col - 2; c >= 0; --c) {
                if (obstacleGrid[r][c] == 1) dp[r][c] = 0;
                else {
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1];
                }
            }
        }

        return dp[0][0];
    }

    public static void main(String[] args) {
        int[][] obstacleGrid = {{0}};
        unique_paths_ii solution = new unique_paths_ii();
        System.out.println(solution.uniquePathsWithObstacles(obstacleGrid));
    }
}