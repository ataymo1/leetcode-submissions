class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        h_map = defaultdict(int)
        h_map[0] = 1

        for num in nums:
            cur_sum += num
            prefix = cur_sum - k
            res += h_map[prefix]

            h_map[cur_sum] += 1
        
        return res

            


        