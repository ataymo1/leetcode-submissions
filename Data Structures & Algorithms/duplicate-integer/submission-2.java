
class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        HashSet<Integer> ns = new HashSet<>();
        for(int i : nums) {
            ns.add(i);
        }

        if(nums.length != ns.size()) {
            return true;
        }

        return false;
        


    }
}
