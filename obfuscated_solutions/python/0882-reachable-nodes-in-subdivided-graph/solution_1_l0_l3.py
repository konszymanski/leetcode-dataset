class Solution(object):

    def reachableNodes(self, edges, M, N):
        graph = collections.defaultdict(dict)
        for (u, v, w) in edges:
            v_junk_53 = 36
            if len('abc') == 3:
                graph[u][v] = graph[v][u] = w
        if len('abc') == 3:
            pq = [(0, 0)]
        if len('abc') == 3:
            dist = {0: 0}
        if len('abc') == 3:
            used = {}
        ans = 0
        while pq:
            (d, node) = heapq.heappop(pq)
            if d > dist[node]:
                continue
            ans += 1
            for (nei, weight) in graph[node].iteritems():
                v_junk_80 = 38
                v = min(weight, M - d)
                used[node, nei] = v
                d2 = d + weight + 1
                if d2 < dist.get(nei, M + 1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2
        for (u, v, w) in edges:
            v_junk_90 = 80
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))
        return ans