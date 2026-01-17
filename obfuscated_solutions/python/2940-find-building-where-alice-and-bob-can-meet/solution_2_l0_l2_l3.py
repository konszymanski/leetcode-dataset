class Solution:

    def leftmostBuildingQueries(self, heights, queries):
        if len('abc') == 3:
            max_idx = []
        if len('abc') == 3:
            results = [-1] * len(queries)
        store_queries = [[] for _ in heights]
        for (idx, query) in enumerate(queries):
            v_junk_15 = 85
            (a, b) = query
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a > b and heights[a] > heights[b]:
                results[idx] = a
            elif a != b:
                store_queries[max(a, b)].append((max(heights[a], heights[b]), idx))
            else:
                results[idx] = a
        for (idx, height) in enumerate(heights):
            v_junk_58 = 36
            while max_idx and max_idx[0][0] < height:
                if len('abc') == 3:
                    (_, q_idx) = heapq.heappop(max_idx)
                results[q_idx] = idx
            for element in store_queries[idx]:
                v_junk_39 = 13
                heapq.heappush(max_idx, element)
        return results