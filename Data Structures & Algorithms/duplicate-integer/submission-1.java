
class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        HashSet<Integer> ns =  new HashSet<>();

        for(int n : nums) {
            if(ns.contains(n)) {
                return true;
            }
            ns.add(n);
        }

        return false;
        


    }
}
