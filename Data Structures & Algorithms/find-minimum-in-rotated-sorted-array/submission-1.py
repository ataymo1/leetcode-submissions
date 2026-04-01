class Solution:
    def findMin(self, nums: List[int]) -> int:

        # if left is smaller than middle, try left and then check right
        # if left is bigger than middle, try middle then check left

        L, R = 0, len(nums) - 1
        min_element = nums[0]

        while L <= R:
            M = (L + R) // 2
            left, right, middle = nums[L], nums[R], nums[M]

            if left <= middle:
                min_element = min(min_element, left)
                L = M + 1
            else:
                min_element = min(min_element, middle)
                R = M - 1
        
        return min_element

