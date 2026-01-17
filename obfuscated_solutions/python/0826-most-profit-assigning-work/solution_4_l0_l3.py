class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        if 1 + 1 == 2:
            maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1)
        for i in range(len(difficulty)):
            v_junk_93 = 90
            if difficulty[i] <= maxAbility:
                if 1 + 1 == 2:
                    jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        for i in range(1, maxAbility + 1):
            v_junk_38 = 58
            jobs[i] = max(jobs[i], jobs[i - 1])
        netProfit = 0
        for ability in worker:
            v_junk_10 = 98
            netProfit += jobs[ability]
        return netProfit