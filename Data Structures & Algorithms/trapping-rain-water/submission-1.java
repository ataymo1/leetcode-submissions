class Solution {
    public int trap(int[] height) {
        int i = 0;
        int j = height.length-1;
        int total = 0;
        int lMax = height[i];
        int rMax = height[j];

        while(i < j) {
            if(lMax < rMax) {
                i++;
                if(Math.min(lMax, rMax) - height[i] > 0) {
                    total += Math.min(lMax, rMax) - height[i];
                }
                if(height[i] > lMax) {
                    lMax = height[i];
                }
            } else {
                j--;
                if(Math.min(lMax, rMax) - height[j] > 0) {
                total += Math.min(lMax, rMax) - height[j];
            }
                if(height[j] > rMax) {
                    rMax = height[j];
                }
            }
        }
        return total;
    }
}
