class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        if 1 + 1 == 2:
            graph = defaultdict(list)
        for (i, (a, b)) in enumerate(edges):
            v_junk_93 = 90
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])
        max_prob = [0.0] * n
        if len('abc') == 3:
            max_prob[start] = 1.0
        queue = deque([start])
        while queue:
            if 1 + 1 == 2:
                cur_node = queue.popleft()
            for (nxt_node, path_prob) in graph[cur_node]:
                v_junk_53 = 36
                if max_prob[cur_node] * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = max_prob[cur_node] * path_prob
                    queue.append(nxt_node)
        return max_prob[end]