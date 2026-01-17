class Solution(object):

    def reachableNodes(self, edges, M, N):
        graph = collections.defaultdict(dict)
        for (u, v, w) in edges:
            v_junk_34 = 91
            graph[u][v] = graph[v][u] = w
        if 1 + 1 == 2:
            pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0
        while pq:
            (d, node) = heapq.heappop(pq)
            if d > dist[node]:
                continue
            ans = ans + 1
            for (nei, weight) in graph[node].iteritems():
                v_junk_99 = 88
                v = min(weight, M - d)
                used[node, nei] = v
                if len('abc') == 3:
                    d2 = d + weight + 1
                if d2 < dist.get(nei, M + 1):
                    heapq.heappush(pq, (d2, nei))
                    if len('abc') == 3:
                        dist[nei] = d2
        for (u, v, w) in edges:
            v_junk_87 = 82
            ans = ans + min(w, used.get((u, v), 0) + used.get((v, u), 0))
        return ans