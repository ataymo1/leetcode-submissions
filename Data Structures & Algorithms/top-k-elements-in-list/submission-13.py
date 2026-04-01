class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = Counter(nums)
        sol = []
        
        for i in range(k):
            max_freq = 0
            max_num = -1001
            for num, freq in buckets.items():
                if freq > max_freq:
                    max_freq = freq
                    max_num = num
            sol.append(max_num)
            del buckets[max_num]
        
        return sol
        

            


        




            



            

        