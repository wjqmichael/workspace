import java.util.*;

public class Solution {
	public int longestConsecutive(int[] num) {
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		int longestSoFar = 0;
		for (int i : num) {
			if (!map.containsKey(i)) {
				map.put(i, 1);
				longestSoFar = Math.max(merge(map, i), longestSoFar);
			}
		}
		return longestSoFar;
	}
	
	private int merge(HashMap<Integer, Integer> map, int i) {
		int leng = 1, left = i, right = i;
		if (map.containsKey(i - 1)) {
			left = i - map.get(i - 1);
			leng += map.get(i - 1);
		}
		if (map.containsKey(i + 1)) {
			right = i + map.get(i + 1);
			leng += map.get(i + 1);
		}
		map.put(left, leng);
		map.put(right, leng);
		return leng;
	}
	
}