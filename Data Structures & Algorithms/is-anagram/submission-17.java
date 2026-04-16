class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> s_chars = new HashMap<>();
        Map<Character, Integer> t_chars = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            s_chars.put(s.charAt(i), s_chars.getOrDefault(s.charAt(i), 0) + 1);
            t_chars.put(t.charAt(i), t_chars.getOrDefault(t.charAt(i), 0) + 1);
        }

        return s_chars.equals(t_chars);
    }
}
