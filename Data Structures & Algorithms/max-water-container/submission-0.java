class Solution {
    public int maxArea(int[] heights) {
        int j = heights.length-1;
        int max = 0;

        for(int i = 0; i < heights.length; i++) {
            if(i == j) {
                break;
            }
            int temp = Math.min(heights[i], heights[j]) * (j-i);
            if(temp > max) {
                max = temp;
            }
            if(heights[i] > heights[j]) {
                i--;
                j--;
            } 
            
        }
        return max;
    }
}
