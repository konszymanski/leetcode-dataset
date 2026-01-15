class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List
        [float], start: int, end: int) ->float:
        max_prob = [0] * n
        max_prob[start] = 1
        i = 0
        while i < n - 1:
            has_update = 0
            for j in range(len(edges)):
                u, v = edges[j]
                path_prob = succProb[j]
                if max_prob[u] * path_prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * path_prob
                    has_update = 1
                if max_prob[v] * path_prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * path_prob
                    has_update = 1
            if not has_update:
                break
            i += 1
        return max_prob[end]
