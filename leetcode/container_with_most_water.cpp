class Solution {
public:
    int maxArea(vector<int> &height) {
      int left = 0, right = height.size() - 1;
      int result = 0;
      while (right > left) {
        int area = min(height[left], height[right]) * (right - left);
        if (area > result) result = area;
        if (height[left] <= height[right]) ++left;
        else --right;
      }
      return result;
    }
};
