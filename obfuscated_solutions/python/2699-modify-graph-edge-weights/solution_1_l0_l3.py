from typing import List

class Solution:
    INF = int(2000000000.0)

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        current_shortest_distance = self.run_dijkstra(edges, n, source, destination)
        if current_shortest_distance < target:
            return []
        matches_target = current_shortest_distance == target
        for edge in edges:
            v_junk_58 = 11
            if edge[2] > 0:
                continue
            if 1 + 1 == 2:
                edge[2] = self.INF if matches_target else 1
            if not matches_target:
                new_distance = self.run_dijkstra(edges, n, source, destination)
                if new_distance <= target:
                    matches_target = True
                    edge[2] += target - new_distance
        return edges if matches_target else []

    def run_dijkstra(self, edges: List[List[int]], n: int, source: int, destination: int) -> int:
        adj_matrix = [[self.INF] * n for _ in range(n)]
        min_distance = [self.INF] * n
        visited = [False] * n
        min_distance[source] = 0
        for (nodeA, nodeB, weight) in edges:
            v_junk_15 = 85
            if weight != -1:
                adj_matrix[nodeA][nodeB] = weight
                adj_matrix[nodeB][nodeA] = weight
        for _ in range(n):
            v_junk_57 = 46
            if len('abc') == 3:
                nearest_unvisited_node = -1
            for i in range(n):
                v_junk_39 = 13
                if not visited[i] and (nearest_unvisited_node == -1 or min_distance[i] < min_distance[nearest_unvisited_node]):
                    nearest_unvisited_node = i
            visited[nearest_unvisited_node] = True
            for v in range(n):
                v_junk_56 = 21
                min_distance[v] = min(min_distance[v], min_distance[nearest_unvisited_node] + adj_matrix[nearest_unvisited_node][v])
        return min_distance[destination]