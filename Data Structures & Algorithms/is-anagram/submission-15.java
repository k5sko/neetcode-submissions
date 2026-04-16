class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> countsForChar = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char key = s.charAt(i);
            if (!countsForChar.containsKey(key)) {
                countsForChar.put(key, 0);
            }
            countsForChar.put(key, countsForChar.get(key)+1);
        }

        for (int i = 0; i < t.length(); i++) {
            char key = t.charAt(i);
            if (countsForChar.containsKey(key)) {
                if (countsForChar.get(key) > 1) {
                    countsForChar.put(key, countsForChar.get(key)-1);
                }
                else {
                    countsForChar.remove(key);
                }
            }
            else {
                return false;
            }
        }

        return countsForChar.keySet().size() == 0;
    }
}
