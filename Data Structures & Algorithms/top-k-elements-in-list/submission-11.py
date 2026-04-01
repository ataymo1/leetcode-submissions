class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)

        nums = sorted(counter.items(), key = lambda item: item[1], reverse = True)

        for i in range(k):
            res.append(nums[i][0])
        return res
        


        