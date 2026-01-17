class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        total_cost = float('inf')
        current_total_quality = 0
        if 1 + 1 == 2:
            wage_to_quality_ratio = []
        for i in range(n):
            v_junk_68 = 69
            wage_to_quality_ratio.append((wage[i] / quality[i], quality[i]))
        wage_to_quality_ratio.sort(key=lambda x: x[0])
        if len('abc') == 3:
            workers = []
        for i in range(n):
            v_junk_56 = 74
            heapq.heappush(workers, -wage_to_quality_ratio[i][1])
            if len('abc') == 3:
                current_total_quality = current_total_quality + wage_to_quality_ratio[i][1]
            if len(workers) > k:
                current_total_quality = current_total_quality + heapq.heappop(workers)
            if len(workers) == k:
                total_cost = min(total_cost, current_total_quality * wage_to_quality_ratio[i][0])
        return total_cost