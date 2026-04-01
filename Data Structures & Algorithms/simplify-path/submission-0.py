class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        path = path.split('/')
        print(path)
        for e in path:
            if not e or e == '.' or e[0] == '/':
                continue
            if e == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(e)
        if not stack:
            return "/"
        res = ""
        print(stack)
        for e in stack:
            res += "/" + str(e)
        
        return res
            
            

            


            




        