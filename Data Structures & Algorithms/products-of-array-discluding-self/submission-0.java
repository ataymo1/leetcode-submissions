class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] pre = new int[nums.length];
        int[] post = new int[nums.length];
        int[] sol = new int[nums.length];
        int ltr = 1;
        int rtl = 1; 
        for(int i = 0; i < nums.length; i++) {
            pre[i] = ltr*nums[i];
            ltr *= nums[i];
        }
        
        for(int i = nums.length-1; i >= 0; i--) {
            post[i] = rtl*nums[i];
            rtl *= nums[i];
        }

        for(int i = 0; i < nums.length; i++) {
            if(i == 0) {
                sol[i] = post[i+1];
            } else if(i == nums.length-1) {
                sol[i] = pre[i-1];
            } else {
                sol[i] = pre[i-1] * post[i+1];
            }
        }
        return sol;
    }
}  
