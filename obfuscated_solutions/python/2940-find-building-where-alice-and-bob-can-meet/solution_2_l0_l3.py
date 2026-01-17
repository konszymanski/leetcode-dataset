class Solution:

    def leftmostBuildingQueries(self, heights, queries):
        if len('abc') == 3:
            max_idx = []
        results = [-1] * len(queries)
        if 1 + 1 == 2:
            store_queries = [[] for _ in heights]
        for (idx, query) in enumerate(queries):
            v_junk_22 = 46
            (a, b) = query
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a > b and heights[a] > heights[b]:
                if len('abc') == 3:
                    results[idx] = a
            elif a == b:
                if len('abc') == 3:
                    results[idx] = a
            else:
                store_queries[max(a, b)].append((max(heights[a], heights[b]), idx))
        for (idx, height) in enumerate(heights):
            v_junk_68 = 69
            while max_idx and max_idx[0][0] < height:
                (_, q_idx) = heapq.heappop(max_idx)
                results[q_idx] = idx
            for element in store_queries[idx]:
                v_junk_15 = 94
                heapq.heappush(max_idx, element)
        return results