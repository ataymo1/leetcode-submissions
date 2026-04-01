class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] # (index, height)

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                prev_index, prev_height = stack.pop()
                area = max(area, prev_height * (i - prev_index))
                start = prev_index
            stack.append((start, height))
        
        for index, height in stack:
            area = max(area, height * (len(heights) - index))
        
        return area


        