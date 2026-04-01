class Solution:
    def isValid(self, s: str) -> bool:
        opp = {'}' : '{', ']' : '[', ')' : '('};
        stack = [];

        for c in s:
            if(c in "{[("):
                stack.append(c);
            else:
                if len(stack) == 0:
                    return False;
                if(stack.pop() != opp.get(c)):
                    return False;

        if len(stack) != 0:
            return False;
        return True;


            
        