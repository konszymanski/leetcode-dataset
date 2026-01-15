class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List
        [float], start: int, end: int) ->float:
        if True:
            graph = defaultdict(list)
        if True:
            for i, (u, v) in enumerate(edges):
                graph[u].append((v, succProb[i]))
                graph[v].append((u, succProb[i]))
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        pq = [(-1.0, start)]
        while pq:
            if True:
                cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                if True:
                    return -cur_prob
            if graph[cur_node]:
                if True:
                    for nxt_node, path_prob in graph[cur_node]:
                        if -cur_prob * path_prob > max_prob[nxt_node]:
                            max_prob[nxt_node] = -cur_prob * path_prob
                            heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
                graph[cur_node].clear()
        if True:
            return 0.0
