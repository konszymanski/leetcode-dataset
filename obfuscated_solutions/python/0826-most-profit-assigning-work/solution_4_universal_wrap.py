class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int],
        worker: List[int]) ->int:
        if True:
            maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1)
        if True:
            for i in range(len(difficulty)):
                if difficulty[i] <= maxAbility:
                    jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        if True:
            for i in range(1, maxAbility + 1):
                jobs[i] = max(jobs[i], jobs[i - 1])
        netProfit = 0
        if True:
            for ability in worker:
                netProfit += jobs[ability]
        if True:
            return netProfit
