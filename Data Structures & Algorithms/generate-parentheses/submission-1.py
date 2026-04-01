class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = "("
        r = ")"
        stack = []
        res = []

        def backtrack(lcount, rcount):

            if lcount+rcount is n*2:
                if(lcount is rcount):
                    print(rcount)
                    print(lcount)
                    res.append("".join(stack))
                return

            if rcount > lcount:
                return
            
            stack.append(l)
            backtrack(lcount+1,rcount)
            stack.pop()

            stack.append(r)
            backtrack(lcount,rcount+1)
            stack.pop()
            
        backtrack(0, 0)
        return res






                


        