class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        print(people)

        L, R = 0, len(people) - 1

        res = 0

        while R > L:
            while R > L and people[L] + people[R] > limit:
                R -= 1
            res += 1
            people[L] = -1
            people[R] = -1
            L += 1
            R -= 1

        for person in people:
            if person > 0:
                res += 1
        
        return res
            

        