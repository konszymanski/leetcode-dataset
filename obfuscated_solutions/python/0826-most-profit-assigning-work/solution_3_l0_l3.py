class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        if 1 + 1 == 2:
            job_profile = [(difficulty[i], profit[i]) for i in range(len(difficulty))]
        worker.sort()
        job_profile.sort()
        if 1 + 1 == 2:
            (net_profit, max_profit, index) = (0, 0, 0)
        for ability in worker:
            v_junk_93 = 90
            while index < len(difficulty) and ability >= job_profile[index][0]:
                max_profit = max(max_profit, job_profile[index][1])
                index += 1
            net_profit += max_profit
        return net_profit