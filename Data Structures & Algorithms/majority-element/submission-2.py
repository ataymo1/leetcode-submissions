class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        element = nums[0]
        counter = 0
        
        # for each element if our counter is 0 then we should switch the element
        for num in nums:
            if counter == 0:
                element = num
            if num == element:
                counter += 1
            else:
                counter -= 1
        
        return element

        # if the current num is our element then increase counter or else decrease it


        