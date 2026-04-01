class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = defaultdict(int)

        for n in nums:
            l[n] += 1;

        sol = [];

        for i in range(k):
            m = 0;
            add = -1;
            for v in l:
                if l.get(v) > m:
                    m = l.get(v);
                    add = v;
            sol.append(add);
            l.pop(add)
        return sol;


            



            

        