class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # go through list with i
        nums.sort();
        sol = [];
        checked = set();
        for i in range(len(nums)-1):
        # go through rest of list with j
            for j in range(i+1, len(nums)):
                numset = set(nums[j+1:])
                key = 0 - (nums[i] + nums[j]);
                l = (nums[i], nums[j], key)
                if key in numset and l not in checked:
                    checked.add(l);
                    sol.append(l);

        return sol;
                    


        # where key = target - i - j
        # check if key is in set