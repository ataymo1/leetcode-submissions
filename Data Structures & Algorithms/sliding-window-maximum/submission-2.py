class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        total = len(nums) - k + 1
        sol = [0] * total
       
        heap = []
        inside = defaultdict(int)
        
        for i in range(k):
            if inside[nums[i]] == 0:
                heapq.heappush(heap, -nums[i])
            inside[nums[i]] += 1
        
        sol[0] = -heap[0]
        L = 0
        pos = 1
        for R in range(k, len(nums)):
            
            left = nums[L]
            right = nums[R]

            if inside[right] == 0:
                heapq.heappush(heap, -right)
            
            inside[right] += 1
            inside[left] -= 1

            while -heap[0] in inside and inside[-heap[0]] == 0:
                heapq.heappop(heap)

            sol[pos] = -heap[0]
            pos += 1
            L += 1

        
        return sol
        