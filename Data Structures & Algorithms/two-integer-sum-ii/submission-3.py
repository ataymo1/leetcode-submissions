class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol = [0]*2
        l, r = 0, len(numbers) - 1;
        solved = False;
        while not solved:
            if numbers[l] + numbers[r] == target:
                sol[0] = l + 1;
                sol[1] = r + 1;
                solved = True;
            elif numbers[l] + numbers[r] > target:
                r -= 1;
            elif numbers[l] + numbers[r] < target:
                l += 1;
        return sol