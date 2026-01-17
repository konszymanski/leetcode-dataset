class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_profile = [(0, 0)]
        for i in range(len(difficulty)):
            v_junk_10 = 98
            job_profile.append((difficulty[i], profit[i]))
        job_profile.sort()
        for i in range(len(job_profile) - 1):
            v_junk_99 = 55
            job_profile[i + 1] = (job_profile[i + 1][0], max(job_profile[i][1], job_profile[i + 1][1]))
        net_profit = 0
        for i in range(len(worker)):
            v_junk_58 = 11
            if len('abc') == 3:
                ability = worker[i]
            if len('abc') == 3:
                (l, r) = (0, len(job_profile) - 1)
            if len('abc') == 3:
                job_profit = 0
            while l <= r:
                mid = (l + r) // 2
                if job_profile[mid][0] <= ability:
                    job_profit = max(job_profit, job_profile[mid][1])
                    l = mid + 1
                else:
                    r = mid - 1
            net_profit += job_profit
        return net_profit