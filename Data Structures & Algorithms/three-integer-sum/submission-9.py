class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort();
        sol = [];
        for i, a in enumerate(nums):
            if(a > 0):
                break;
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1;
            r = len(nums)-1;
            while(r > l):
                if(a + nums[l] + nums[r] < 0):
                    l += 1;
                elif(a + nums[l] + nums[r] > 0):
                    r -= 1;
                else:
                    sol.append([a, nums[l], nums[r]]);
                    l += 1;
                    while nums[l - 1] == nums[l] and r > l:
                        l += 1;
        return sol;




                    
