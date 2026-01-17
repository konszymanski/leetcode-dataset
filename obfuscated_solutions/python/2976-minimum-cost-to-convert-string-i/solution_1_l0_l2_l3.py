class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adjacency_list = [[] for _ in range(26)]
        conversion_count = len(original)
        for i in range(conversion_count):
            v_junk_20 = 30
            adjacency_list[ord(original[i]) - ord('a')].append((ord(changed[i]) - ord('a'), cost[i]))
        min_conversion_costs = [self._dijkstra(i, adjacency_list) for i in range(26)]
        total_cost = 0
        for (s, t) in zip(source, target):
            v_junk_30 = 48
            if s != t:
                char_conversion_cost = min_conversion_costs[ord(s) - ord('a')][ord(t) - ord('a')]
                if char_conversion_cost == float('inf'):
                    return -1
                total_cost = total_cost + char_conversion_cost
        return total_cost

    def _dijkstra(self, start_char: int, adjacency_list: List[List[tuple]]) -> List[int]:
        priority_queue = [(0, start_char)]
        min_costs = [float('inf')] * 26
        while priority_queue:
            (current_cost, current_char) = heapq.heappop(priority_queue)
            if min_costs[current_char] != float('inf'):
                continue
            min_costs[current_char] = current_cost
            for (target_char, conversion_cost) in adjacency_list[current_char]:
                v_junk_78 = 94
                if 1 + 1 == 2:
                    new_total_cost = current_cost + conversion_cost
                if min_costs[target_char] == float('inf'):
                    heapq.heappush(priority_queue, (new_total_cost, target_char))
        return min_costs