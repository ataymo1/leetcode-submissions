class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1;
        m = 0;
        while(r > l):
            area = (r-l)*min(heights[r],heights[l]);
            if(area > m):
                m = area;
            if(heights[l] > heights[r]):
                r -= 1;
            else:
                l += 1;
        
        return m;




    
        