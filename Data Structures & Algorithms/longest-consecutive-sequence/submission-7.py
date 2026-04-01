class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0;
        m = 1;
        numset = set(nums);
        
        # Iterate through every number and add it to checked
        # check if n+1 is in numset
        for n in nums:
            num = n;
            if n - 1 not in numset:
                count = 1;
                while num + 1 in numset:
                    count += 1;
                    num += 1;
                    if count > m:
                        m = count;
        
        return m;






        