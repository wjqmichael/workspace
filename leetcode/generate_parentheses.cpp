class Solution {
public:
    vector<string> generateParenthesis(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
      vector<string> result;
      helper(result, "", 0, 0, n);
      return result;
    }
    void helper(vector<string>& result, string current, int l, int r, int n) {
      if (l == n && r == n) {
        result.push_back(current);
        return;
      }
      if (l > r) helper(result, current + ")", l, r + 1, n);
      if (l < n) helper(result, current + "(", l + 1, r, n);
    }
};
