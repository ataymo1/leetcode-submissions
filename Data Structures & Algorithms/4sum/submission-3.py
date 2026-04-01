class Solution:

    # Sort - >
    # 1st Pointer
    # move pointer towards end
    #     stop if greater
    #     if equal
    #         add to list as set
    # move 1st, 2nd to original + 1
    #     same alg
    # move 1st, 2nd, 3rd to original + 1
    #     same alg
    # move 1st, 2nd, 3rd to original + 1
    #     same alg
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        if len(nums) < 4:
            return [[]]
        
        sol = set()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums) - 2):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur_sum == target:
                        sol.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif cur_sum > target:
                        right -= 1
                    else:
                        left += 1


        return list(sol)
                
        

        