class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0 for i in range(n+1)]

        for i in range(n+1):
            print(i)
            arr[i] = i.bit_count()
        
        return arr
        