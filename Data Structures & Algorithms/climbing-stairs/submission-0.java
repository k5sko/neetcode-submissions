class Solution {
    public int climbStairs(int n) {
        int steps = 0;
        if (n < 0) {
            return 0;
        }
        if (n == 0) {
            return 1;
        }

        steps += climbStairs(n-1);
        steps += climbStairs(n-2);

        return steps;
    }
}
