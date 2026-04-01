class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        length = len(digits)

        digit_to_letter = {
            2 : 'abc',
            3 : 'def',
            4 : 'ghi',
            5 : 'jkl',
            6 : 'mno',
            7 : 'pqrs',
            8 : 'tuv',
            9 : 'wxyz'
        }

        def backtrack(index, cur_str):
            if len(cur_str) == length:
                temp = ""
                for c in cur_str:
                    temp += c
                if temp:
                    res.append(temp)
                return

            if index > len(cur_str):
                return

            cur_digit = int(digits[index])

            for c in digit_to_letter[cur_digit]:
                cur_str.append(c)
                backtrack(index + 1, cur_str)
                cur_str.pop()


        backtrack(0, [])

        return res
        