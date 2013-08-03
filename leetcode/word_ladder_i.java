import java.util.*;

public class Solution {
	public int ladderLength(String start, String end, HashSet<String> dict) {
		if (start == end) return 0;
		int leng = 1;
		ArrayList<String> nxt = new ArrayList<String>();
		nxt.add(start);
		while (!nxt.isEmpty()) {
			ArrayList<String> tmp = new ArrayList<String>();
			for (String s : nxt) {
				if (dist(s, end) == 1) return 1 + leng;
				getNextLeng(s, tmp, dict);
			}
			nxt = tmp;
			++leng;
		}
		return 0;
	}
	
	public static void getNextLeng(String s, ArrayList<String> cur, HashSet<String> dict) {		
		StringBuilder sb = new StringBuilder(s);
		for (int i = 0; i < s.length(); ++i) {
			for (int j = 0; j < 26; ++j) {
				if (s.charAt(i) != 'a' + j) {
					sb.setCharAt(i, (char) ('a' + j));
					if (dict.contains(sb.toString())) {
						dict.remove(sb.toString());
						cur.add(sb.toString());
					}
				}
			}
			sb.setCharAt(i, s.charAt(i));
		}
	}	
		/*Iterator<String> it = dict.iterator();
		while (it.hasNext()) {
			String sd = it.next();
			if (dist(s, sd) == 1) {
				cur.add(sd);
				it.remove();
			}
		}
	}*/
	
	public static int dist(String s1, String s2) {
		int count = 0;
		for (int i = 0; i < Math.min(s1.length(), s2.length()); ++i) {
			if (s1.charAt(i) != s2.charAt(i)) ++count;
		}
		return count;
	}
	
	public static void main(String[] args) {
		ArrayList<String> al = new ArrayList<String>();
		al.add("hot"); 
		System.out.println(dist("abc", "abde"));
	}
}


