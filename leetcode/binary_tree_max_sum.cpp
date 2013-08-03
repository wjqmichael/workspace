/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  int maxPathSumHelper(TreeNode* node, int& maxSum) {
    if (!node) return INT_MIN;
    int lMax = maxPathSumHelper(node->left, maxSum);
    int rMax = maxPathSumHelper(node->right, maxSum);

  }

  int
  maxPathSum(TreeNode *root) {
    // Start typing your C/C++ solution below
    // DO NOT write int main() function

  }
};
