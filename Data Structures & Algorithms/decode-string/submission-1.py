class Solution:
    def decodeString(self, s: str) -> str:

        # when k is found, start a stack with a number
        # when ] is found, pop the stack and multiply string by that number
        # if stack is empty, make current string blank
        res = ""
        cur_s = ""
        stack = []
        skip = 0
        for i, c in enumerate(s):
            if skip > 0:
                skip -= 1
                continue
            if c == '[':
                continue
            elif c.isdigit():
                if i + 1 < len(s) and s[i+1].isdigit():
                    skip += 1
                    if i + 2 < len(s) and s[i+2].isdigit():
                        skip += 1
                        stack.append((int(s[i:i+3]), cur_s))
                    else:
                        stack.append((int(s[i:i+2]), cur_s))
                else:
                    stack.append((int(c), cur_s))
                cur_s = ""
                continue
            elif c == ']':
                multiplier, prev_s = stack.pop()
                cur_s *= multiplier
                if not stack:
                    res += cur_s
                    cur_s = ""
                else:
                    cur_s = prev_s + cur_s

            else:
                if stack:
                    cur_s += c
                else:
                    res += c
        return res




        