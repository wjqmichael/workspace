import java.util.*;

public class valid_parentheses{
    private HashMap<Character, Character> getMatch() {
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
        return map;
    }

    public boolean isValid(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        HashMap<Character, Character> match = getMatch();
        Stack<Character> st = new Stack<Character>();
        for (char ch : s.toCharArray()) {
            if (match.containsKey(ch)) st.push(ch);
            else {
                if (st.isEmpty()) return false;
                if (match.get(st.pop()) != ch) return false;
            }
        }
        return st.isEmpty() ? true : false;
    }

    public static void main(String[] args) {
        valid_parentheses v = new valid_parentheses();
        System.out.println(v.isValid("(())"));
    }
}