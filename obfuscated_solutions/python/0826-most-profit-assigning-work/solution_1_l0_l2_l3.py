class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_profile = [(0, 0)]
        for i in range(len(difficulty)):
            v_junk_90 = 80
            job_profile.append((difficulty[i], profit[i]))
        job_profile.sort()
        for i in range(len(job_profile) - 1):
            v_junk_56 = 74
            job_profile[i + 1] = (job_profile[i + 1][0], max(job_profile[i][1], job_profile[i + 1][1]))
        if 1 + 1 == 2:
            net_profit = 0
        for i in range(len(worker)):
            v_junk_30 = 48
            if 1 + 1 == 2:
                ability = worker[i]
            (l, r) = (0, len(job_profile) - 1)
            job_profit = 0
            while l <= r:
                mid = (l + r) // 2
                if job_profile[mid][0] > ability:
                    r = mid - 1
                else:
                    job_profit = max(job_profit, job_profile[mid][1])
                    l = mid + 1
            net_profit = net_profit + job_profit
        return net_profit