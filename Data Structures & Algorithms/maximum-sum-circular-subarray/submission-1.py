class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = nums[0]
        cur_min = nums[0]
        cur_max_sum = 0
        cur_min_sum = 0
        total = 0
        
        for n in nums:
            cur_max_sum = max(cur_max_sum, 0) + n
            cur_min_sum = min(cur_min_sum, 0) + n

            global_max = max(cur_max_sum, global_max)
            cur_min = min(cur_min_sum, cur_min)
            total += n

        if global_max < 0:
            return global_max

        return total - cur_min if total - cur_min > global_max else global_max





