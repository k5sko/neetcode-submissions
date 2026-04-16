class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> s_chars = new HashMap<>();
        Map<Character, Integer> t_chars = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (s_chars.keySet().contains(s.charAt(i))) {
                s_chars.put(s.charAt(i), s_chars.get(s.charAt(i)) + 1);
            }
            else {
                s_chars.put(s.charAt(i), 0);
            }

            if (t_chars.keySet().contains(t.charAt(i))) {
                t_chars.put(t.charAt(i), t_chars.get(t.charAt(i)) + 1);
            }
            else {
                t_chars.put(t.charAt(i), 0);
            }
        }

        return s_chars.equals(t_chars);
    }
}
