class Solution {
    public boolean isPalindrome(String s) {
        int f = 0;
        int b = s.length() - 1;

        while (f < b && f < s.length() && b >= 0) {
            System.out.println("f: " + f + "\nb: " + b + "\nchar f: " + Character.toUpperCase(s.charAt(f)) + "\n");
            char f_char = Character.toUpperCase(s.charAt(f));
            if ((Character.toUpperCase(f_char) < 'A' || Character.toUpperCase(f_char) > 'Z') && (f_char < '0' || f_char > '9')) {
                f++;
                continue;
            }
            char b_char = Character.toUpperCase(s.charAt(b));
            if ((Character.toUpperCase(b_char) < 'A' || Character.toUpperCase(b_char) > 'Z') && (b_char < '0' || b_char > '9')) {
                b--;
                continue;
            }

            if (f_char != b_char) {
                return false;
            }
            f++;
            b--;

        }

        return true;
    }
}
