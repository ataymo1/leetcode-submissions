class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        e1, e2 = None, None
        counter1 = 0
        counter2 = 0
        res = []
        length = len(nums)

        for num in nums:
            print(f"{e1} : {e2}")
            
            if num == e1:
                counter1 += 1
                continue
            elif num == e2:
                counter2 += 1
                continue
            elif counter1 == 0:
                e1 = num
                counter1 = 1
            elif counter2 == 0:
                e2 = num
                counter2 = 1
            else:
                counter1 -= 1
                counter2 -= 1
            
        counter1 = 0
        counter2 = 0

        for num in nums:
            if num == e1:
                counter1 += 1
            elif num == e2:
                counter2 += 1
        
        if counter1 > length // 3:
            res.append(e1)
        
        if counter2 > length // 3:
            res.append(e2)
        
        return res

         
                

        
        

        
