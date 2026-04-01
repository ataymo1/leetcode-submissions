class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white = 0, 0

        for blue in range(len(nums)):
            color = nums[blue]
            nums[blue] = 2

            if color == 0:
                nums[white] = 1
                nums[red] = 0
                red += 1
                white += 1
            if color == 1:
                nums[white] = 1
                white += 1
            
            
            
                

        