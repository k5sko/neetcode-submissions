class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = cleanString(s);

        String reversed = reverseString(s);
        return s.equals(reversed);
    }

    private String cleanString (String s) {
        String newStr = new String();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z' || c >= '0' && c <= '9') {
                newStr += c;
            }
        }

        return newStr;
    }

    private String reverseString(String s) {
        String reversed = new String();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            reversed = c + reversed;
        }
        return reversed;
    }
}
