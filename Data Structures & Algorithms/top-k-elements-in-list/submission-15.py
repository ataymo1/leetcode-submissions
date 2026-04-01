class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        sol = []
        buckets = [[] for i in range(len(nums) + 1)]

        counter = Counter(nums)

        for num, freq in counter.items():
            buckets[freq].append(num)
        
        i = len(nums) - 1

        while k > 0:
            while buckets[i] and k > 0:
                sol.append(buckets[i].pop())
                k -= 1
            i -= 1
        
        return sol

            

        