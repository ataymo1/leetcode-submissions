class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        diff_jobs = [0] * 26

        for i in range(len(tasks)):
            diff_jobs[ord('A') - ord(tasks[i])] += 1
        
        print(diff_jobs)
        max_frequency = max(diff_jobs)
        jobs_with_max = 0

        for i in range(len(diff_jobs)):
            jobs_with_max += 1 if diff_jobs[i] == max_frequency else 0

        print(f"{max_frequency} : {n} : {jobs_with_max}")
        
        return max((max_frequency - 1) * (n + 1) + jobs_with_max, len(tasks))



        







        