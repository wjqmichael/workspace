/**
 * Definition for binary tree public class TreeNode { int val; TreeNode left;
 * TreeNode right; TreeNode(int x) { val = x; } }
 */

public class Solution {
	public int sumNumbers(TreeNode root) {
		// Start typing your Java solution below
		// DO NOT write main() function
		return helper(root, 0);
	}

	private int helper(TreeNode root, int soFar) {
		if (root == null) return 0;
		int temp = root.val + soFar * 10;
		if (root.left == null && root.right == null) return temp;
		return helper(root.left, temp) + helper(root.right, temp);
	}
}