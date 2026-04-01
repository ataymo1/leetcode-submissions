class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        buckets = [[] for _ in range(len(nums))]

        counter = Counter(nums)

        for key, value in counter.items():
            buckets[value-1].append(key)

        i = len(nums) - 1

        while k > 0:
            print(buckets[i])
            while buckets[i] and k > 0:
                res.append(buckets[i].pop())
                k -= 1;
            i -= 1;
        
        return res




        


        