import java.util.*;

public class Solution {
	public ArrayList<ArrayList<String>> partition(String s) {
		ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
		if (s.isEmpty()) {
			result.add(new ArrayList<String>());
			return result;
		}
		int leng = s.length();
		for (int i = 1; i <= leng; ++i) {
			String left = s.substring(0, i);
			if (!isPalindrome(left)) continue;
			ArrayList<ArrayList<String>> right = partition(s.substring(i));
			for (ArrayList<String> l : right) {
				l.add(0, left);
				result.add(l);
			}
		}
		return result;
	}
	
	private boolean isPalindrome(String s) {
		for (int left = 0, right = s.length() - 1; left < right; ++left, --right) {
			if (s.charAt(left) != s.charAt(right)) return false;
		}
		return true;
	}
}