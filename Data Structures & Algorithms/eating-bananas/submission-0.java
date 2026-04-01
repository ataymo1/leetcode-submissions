class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        Arrays.sort(piles);
        int l = 1;
        int r = piles[piles.length-1];

        while(l < r) {
            int mid = (l + r) / 2;
            int hours = 0;
            for(int p : piles) {
                hours += Math.ceil((double)p/mid);
            }
            if(hours > h) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
        
    }
}
