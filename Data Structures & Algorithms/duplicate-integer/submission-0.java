class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numsSet = new HashSet<Integer>();
        for (int i : nums) {
            numsSet.add(i);
        }
        return numsSet.size() != nums.length;
    }
}