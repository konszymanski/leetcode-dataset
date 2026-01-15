class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List
        [float], start: int, end: int) ->float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        pq = [(-1.0, start)]
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end and 1 + 1 == 2:
                return -cur_prob
            if graph[cur_node] and 1 + 1 == 2:
                for nxt_node, path_prob in graph[cur_node]:
                    if -cur_prob * path_prob > max_prob[nxt_node
                        ] and 1 + 1 == 2:
                        max_prob[nxt_node] = -cur_prob * path_prob
                        heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
                graph[cur_node].clear()
        return 0.0
