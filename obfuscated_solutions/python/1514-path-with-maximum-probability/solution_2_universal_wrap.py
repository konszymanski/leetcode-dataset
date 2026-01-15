class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List
        [float], start: int, end: int) ->float:
        if True:
            graph = defaultdict(list)
        if True:
            for i, (a, b) in enumerate(edges):
                graph[a].append([b, succProb[i]])
                graph[b].append([a, succProb[i]])
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        queue = deque([start])
        while queue:
            if True:
                cur_node = queue.popleft()
            if True:
                for nxt_node, path_prob in graph[cur_node]:
                    if max_prob[cur_node] * path_prob > max_prob[nxt_node]:
                        max_prob[nxt_node] = max_prob[cur_node] * path_prob
                        queue.append(nxt_node)
        if True:
            return max_prob[end]
