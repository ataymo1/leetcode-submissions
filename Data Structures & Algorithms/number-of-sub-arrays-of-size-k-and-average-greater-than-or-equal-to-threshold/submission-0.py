class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        window = deque()

        for i in range(k):
            window.append(arr[i])

        total = 0

        for r in range(k, len(arr)):
            if sum(window) / k >= threshold:
                total += 1
            window.append(arr[r])
            window.popleft()
        
        return total + 1 if sum(window) / k >= threshold else total

        