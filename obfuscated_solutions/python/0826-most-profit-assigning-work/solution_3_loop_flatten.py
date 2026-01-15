class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int],
        worker: List[int]) ->int:
        job_profile = [(difficulty[i], profit[i]) for i in range(len(
            difficulty))]
        worker.sort()
        job_profile.sort()
        net_profit, max_profit, index = 0, 0, 0
        for ability in worker:
            while True:
                if not (index < len(difficulty) and ability >= job_profile[
                    index][0]):
                    break
                max_profit = max(max_profit, job_profile[index][1])
                index += 1
            net_profit += max_profit
        return net_profit
