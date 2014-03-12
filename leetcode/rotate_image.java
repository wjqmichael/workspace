public class Solution {
    private void rotate_elem(int[][] matrix, int i, int j) {
        int n = matrix.length;
        int tmp = matrix[i][j];
        matrix[i][j] = matrix[n - 1 - j][i];
        matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
        matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
        matrix[j][n - 1 - i] = tmp;
    }

    public void rotate(int[][] matrix) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int n = matrix.length;
        for (int i = 0; i < n/2; ++i) {
            for (int j = i; j < n - 1 - i; ++j) {
                rotate_elem(matrix, i, j);
            }
        }
    }
}