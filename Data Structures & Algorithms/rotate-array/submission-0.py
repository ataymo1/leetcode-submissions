class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0: return

        for i in range(n // 2):
            temp = nums[n-1-i]
            nums[n-1-i] = nums[i]
            nums[i] = temp

        for i in range(k // 2):
            temp = nums[k-1-i]
            nums[k-1-i] = nums[i]
            nums[i] = temp

        for i in range((n - k) // 2):
            temp = nums[-1-i]
            nums[-1-i] = nums[k+i]
            nums[k+i] = temp
