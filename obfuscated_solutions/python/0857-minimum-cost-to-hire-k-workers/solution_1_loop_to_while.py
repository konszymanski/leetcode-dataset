class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int
        ) ->float:
        n = len(quality)
        total_cost = float('inf')
        current_total_quality = 0
        wage_to_quality_ratio = []
        i = 0
        while i < n:
            wage_to_quality_ratio.append((wage[i] / quality[i], quality[i]))
            i += 1
        wage_to_quality_ratio.sort(key=lambda x: x[0])
        workers = []
        i = 0
        while i < n:
            heapq.heappush(workers, -wage_to_quality_ratio[i][1])
            current_total_quality += wage_to_quality_ratio[i][1]
            if len(workers) > k:
                current_total_quality += heapq.heappop(workers)
            if len(workers) == k:
                total_cost = min(total_cost, current_total_quality *
                    wage_to_quality_ratio[i][0])
            i += 1
        return total_cost
