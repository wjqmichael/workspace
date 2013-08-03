public class Solution {
	public void solve(char[][] board) {
		int row = board.length;
		if (row == 0) return;
		int col = board[0].length;
		boolean[][] mark = new boolean[row][col];
		for (int i = 0; i < col; ++i) {
			mark(board, mark, 0, i);
			mark(board, mark, row - 1, i);
		}
		for (int i = 1; i < row - 1; ++i) {
			mark(board, mark, i, 0);
			mark(board, mark, i, col - 1);
		}
		flip(board, mark);
	}

	private void mark(char[][] board, boolean[][] mark, int r, int c) {
		int row = board.length;
		int col = board[0].length;
		if (r < 0 || r >= row) return;
		if (c < 0 || c >= col) return;
		if (board[r][c] == 'X') return;
		if (mark[r][c] == true) return;

		mark[r][c] = true;
		if (r != 0 && r != row - 1) {
			mark(board, mark, r + 1, c);
			mark(board, mark, r - 1, c);
		}
		if (c != 0 && c != col - 1) {
			mark(board, mark, r, c + 1);
			mark(board, mark, r, c - 1);
		}
	}

	private void flip(char[][] board, boolean[][] mark) {
		int row = board.length;
		int col = board[0].length;
		for (int i = 0; i != row; ++i) {
			for (int j = 0; j != col; ++j) {
				if (board[i][j] == 'O' && mark[i][j] == false) board[i][j] = 'X';
			}
		}
	}

	public static void main(String[] args) {
		char[][] board = {"OO".toCharArray(), "OO".toCharArray()};
		Solution s = new Solution();
		s.solve(board);
		for (char[] i : board) {
			for (char j : i) {
				System.out.print(j + " ");
			}
			System.out.println();
		}
	}
}