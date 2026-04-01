class Solution:
    def reverseBits(self, n: int) -> int:

        copy = 0


        for i in range(32):
            copy = copy ^ ((n & 1) << 31-i)
            n = n >> 1
        
        return copy


        