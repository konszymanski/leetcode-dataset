class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int],
        worker: List[int]) ->int:
        maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1)
        i = 0
        while i < len(difficulty):
            if difficulty[i] <= maxAbility:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
            i += 1
        i = 1
        while i < maxAbility + 1:
            jobs[i] = max(jobs[i], jobs[i - 1])
            i += 1
        netProfit = 0
        for ability in worker:
            netProfit += jobs[ability]
        return netProfit
