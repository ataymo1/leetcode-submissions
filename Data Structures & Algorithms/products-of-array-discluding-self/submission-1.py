class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = [0]*len(nums);
        r = [0]*len(nums);
        sol = [0]*len(nums);

        # 1, 2, 4, 6

        # LTR 1, 2, 8, 48

        # RTL 48, 48, 24, 6

        count = 1;
        for i in range(len(nums)):
            count *= nums[i];
            l[i] = count;

        count = 1;
        for i in range(len(nums)-1, -1, -1):
            count *= nums[i];
            r[i] = count;
        
        for i in range(len(nums)):
            if i == 0:
                sol[i] = r[1];
            elif i == len(nums)-1:
                sol[i] = l[len(nums) - 2];
            else:
                sol[i] = l[i-1] * r[i+1];

        return sol;


        

        

        