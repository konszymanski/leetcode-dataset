class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) ->int:
        pq = []
        i = 0
        while i < candidates:
            pq.append((costs[i], 0))
            i += 1
        i = max(candidates, len(costs) - candidates)
        while i < len(costs):
            pq.append((costs[i], 1))
            i += 1
        heapify(pq)
        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates
        _ = 0
        while _ < k:
            cur_cost, cur_section_id = heappop(pq)
            answer += cur_cost
            if next_head <= next_tail:
                if cur_section_id == 0:
                    heappush(pq, (costs[next_head], 0))
                    next_head += 1
                else:
                    heappush(pq, (costs[next_tail], 1))
                    next_tail -= 1
            _ += 1
        return answer
