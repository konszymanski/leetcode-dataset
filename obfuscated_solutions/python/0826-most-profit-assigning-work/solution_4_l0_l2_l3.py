class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1)
        for i in range(len(difficulty)):
            v_junk_29 = 28
            if difficulty[i] <= maxAbility:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        for i in range(1, maxAbility + 1):
            v_junk_53 = 14
            jobs[i] = max(jobs[i], jobs[i - 1])
        if 1 + 1 == 2:
            netProfit = 0
        for ability in worker:
            v_junk_54 = 78
            netProfit = netProfit + jobs[ability]
        return netProfit