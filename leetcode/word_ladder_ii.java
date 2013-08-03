import java.util.*;

public class Solution {
	public static ArrayList<ArrayList<String>> findLadders(String start,
			String end, HashSet<String> dict) {
		ArrayList<String> cur = new ArrayList<String>();
		cur.add(start);
		HashMap<String, HashSet<String>> neighbors = new HashMap<String, HashSet<String>>();
		boolean stop = false;
		while (!cur.isEmpty()) {
			HashSet<String> nxt = new HashSet<String>();
			HashMap<String, HashSet<String>> tmpMap = new HashMap<String, HashSet<String>>();
			for (String s : cur) {
				if (getNeighbors(s, end, dict, nxt, neighbors, tmpMap)) stop = true;
			}
			cur = new ArrayList<String>(nxt);
			neighbors.putAll(tmpMap);
			if (stop == true) {
				//System.out.println(neighbors);
				return print(end, start, neighbors);
			}
		}
		return new ArrayList<ArrayList<String>>();
	}

	public static ArrayList<ArrayList<String>> print(String s, String start,
			HashMap<String, HashSet<String>> path) {
		ArrayList<ArrayList<String>> ret = new ArrayList<ArrayList<String>>();
		if (s.equals(start)) {
			ArrayList<String> elem = new ArrayList<String>();
			elem.add(s);
			ret.add(elem);
			return ret;
		}

		HashSet<String> neighbors = path.get(s);
		if (neighbors != null) {
			for (String sn : neighbors) {
				ArrayList<ArrayList<String>> tmp = print(sn, start, path);
				for (ArrayList<String> al : tmp) {
					al.add(s);
				}
				ret.addAll(tmp);
			}
		}
		return ret;
	}

	public static boolean getNeighbors(String s, String end,
			HashSet<String> dict, HashSet<String> nxt,
			HashMap<String, HashSet<String>> neighbors,
			HashMap<String, HashSet<String>> tmpMap) {
		StringBuilder sb = new StringBuilder(s);
		boolean hitEnd = false;
		for (int i = 0; i < s.length(); ++i) {
			for (int j = 0; j < 26; ++j) {
				if (s.charAt(i) != 'a' + j) {
					sb.setCharAt(i, (char) ('a' + j));
					String tmp = sb.toString();
					if (tmp.equals(end)) hitEnd = true;
					if (dict.contains(tmp) && !neighbors.containsKey(tmp)) { // || tmp == end) {
						nxt.add(tmp);
						if (tmpMap.containsKey(tmp)) tmpMap.get(tmp).add(s);
						else tmpMap.put(tmp, new HashSet<String>(Arrays.asList(s)));
					}
				}
			}
			sb.setCharAt(i, s.charAt(i)); // reset sb
		}
		return hitEnd;
	}

	public static void main(String[] args) {
		System.out.println("hello world");
		HashSet<String> hs = new HashSet<String>(Arrays.asList("hot", "dot", "dog",
				"lot", "log", "cog", "hog"));
		System.out.println("dict = " + hs);
		System.out.println(findLadders("hot", "dog", hs));
	}
}