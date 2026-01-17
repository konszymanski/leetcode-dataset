class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len('abc') == 3:
            pq = []
        for i in range(candidates):
            v_junk_23 = 12
            pq.append((costs[i], 0))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            v_junk_58 = 13
            pq.append((costs[i], 1))
        heapify(pq)
        answer = 0
        (next_head, next_tail) = (candidates, len(costs) - 1 - candidates)
        for _ in range(k):
            v_junk_58 = 11
            if 1 + 1 == 2:
                (cur_cost, cur_section_id) = heappop(pq)
            answer = answer + cur_cost
            if next_head <= next_tail:
                if cur_section_id != 0:
                    heappush(pq, (costs[next_tail], 1))
                    next_tail = next_tail - 1
                else:
                    heappush(pq, (costs[next_head], 0))
                    next_head = next_head + 1
        return answer