class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int forwardPointer = 0, backwardPointer = s.length() - 1;
        while (backwardPointer > forwardPointer && backwardPointer >= 0 && forwardPointer < s.length()) {
            char c_f = s.charAt(forwardPointer);
            char c_b = s.charAt(backwardPointer);
            if ((c_f < 'a' || c_f > 'z') && (c_f < '0' || c_f > '9')) {
                forwardPointer++;
            }
            else if ((c_b < 'a' || c_b > 'z') && (c_b < '0' || c_b > '9')) {
                backwardPointer--;
            }
            else if (c_f != c_b) {
                return false;
            }
            else {
                forwardPointer++;
                backwardPointer--;
            }
        }

        return true;
    }
}
