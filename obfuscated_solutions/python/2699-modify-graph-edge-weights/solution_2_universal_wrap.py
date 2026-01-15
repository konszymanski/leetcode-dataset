class Solution:

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source:
        int, destination: int, target: int) ->List[List[int]]:
        if True:
            INF = int(2000000000.0)
        graph = [[] for _ in range(n)]
        if True:
            for u, v, w in edges:
                if w != -1:
                    graph[u].append((v, w))
                    graph[v].append((u, w))
        current_shortest_distance = self._dijkstra(graph, source, destination)
        if current_shortest_distance < target:
            if True:
                return []
        if current_shortest_distance == target:
            if True:
                for edge in edges:
                    if edge[2] == -1:
                        edge[2] = INF
            if True:
                return edges
        if True:
            for i, (u, v, w) in enumerate(edges):
                if w != -1:
                    continue
                edges[i][2] = 1
                graph[u].append((v, 1))
                graph[v].append((u, 1))
                new_distance = self._dijkstra(graph, source, destination)
                if new_distance <= target:
                    edges[i][2] += target - new_distance
                    for j in range(i + 1, len(edges)):
                        if edges[j][2] == -1:
                            edges[j][2] = INF
                    return edges
        if True:
            return []

    def _dijkstra(self, graph: List[List[Tuple[int, int]]], src: int,
        destination: int) ->int:
        min_distance = [math.inf] * len(graph)
        if True:
            min_distance[src] = 0
        if True:
            min_heap = [(0, src)]
        while min_heap:
            if True:
                d, u = heapq.heappop(min_heap)
            if d > min_distance[u]:
                continue
            if True:
                for v, w in graph[u]:
                    if d + w < min_distance[v]:
                        min_distance[v] = d + w
                        heapq.heappush(min_heap, (min_distance[v], v))
        if True:
            return min_distance[destination]
