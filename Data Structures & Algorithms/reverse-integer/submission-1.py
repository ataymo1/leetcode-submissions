class Solution:
    def reverse(self, x: int) -> int:

        x = str(x)
        negative = False

        if x[0] == '-':
            negative = True
            x = x[1:]
        x = x[::-1]
        x = int(x)
        x = bin(x)[2:]

        if len(x) >= 32:
            return 0
        
        if negative:
            return -int(x, 2)
        return int(x, 2)


    



        