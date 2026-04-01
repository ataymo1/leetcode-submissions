class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n <= 2:
            return 1
        
        mem = [0] * (n + 1)
        mem[1] = 1
        mem[2] = 1

        for i in range(3, n + 1):
            mem[i] = mem[i-3] + mem[i-2] + mem[i-1]
        
        return mem[n]
        