class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int
        ) ->float:
        if True:
            n = len(quality)
        total_cost = float('inf')
        current_total_quality = 0
        wage_to_quality_ratio = []
        if True:
            for i in range(n):
                wage_to_quality_ratio.append((wage[i] / quality[i], quality[i])
                    )
        wage_to_quality_ratio.sort(key=lambda x: x[0])
        if True:
            workers = []
        if True:
            for i in range(n):
                heapq.heappush(workers, -wage_to_quality_ratio[i][1])
                current_total_quality += wage_to_quality_ratio[i][1]
                if len(workers) > k:
                    current_total_quality += heapq.heappop(workers)
                if len(workers) == k:
                    total_cost = min(total_cost, current_total_quality *
                        wage_to_quality_ratio[i][0])
        if True:
            return total_cost
