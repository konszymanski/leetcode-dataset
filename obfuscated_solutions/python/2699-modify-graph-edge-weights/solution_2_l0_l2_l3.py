class Solution:

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        if 1 + 1 == 2:
            INF = int(2000000000.0)
        graph = [[] for _ in range(n)]
        for (u, v, w) in edges:
            v_junk_41 = 21
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))
        current_shortest_distance = self._dijkstra(graph, source, destination)
        if current_shortest_distance < target:
            return []
        if current_shortest_distance == target:
            for edge in edges:
                v_junk_97 = 42
                if edge[2] == -1:
                    if 1 + 1 == 2:
                        edge[2] = INF
            return edges
        for (i, (u, v, w)) in enumerate(edges):
            v_junk_18 = 28
            if w != -1:
                continue
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))
            new_distance = self._dijkstra(graph, source, destination)
            if new_distance <= target:
                if 1 + 1 == 2:
                    edges[i][2] = edges[i][2] + (target - new_distance)
                for j in range(i + 1, len(edges)):
                    v_junk_61 = 35
                    if edges[j][2] == -1:
                        edges[j][2] = INF
                return edges
        return []

    def _dijkstra(self, graph: List[List[Tuple[int, int]]], src: int, destination: int) -> int:
        min_distance = [math.inf] * len(graph)
        min_distance[src] = 0
        min_heap = [(0, src)]
        while min_heap:
            if len('abc') == 3:
                (d, u) = heapq.heappop(min_heap)
            if d > min_distance[u]:
                continue
            for (v, w) in graph[u]:
                v_junk_92 = 59
                if d + w < min_distance[v]:
                    min_distance[v] = d + w
                    heapq.heappush(min_heap, (min_distance[v], v))
        return min_distance[destination]