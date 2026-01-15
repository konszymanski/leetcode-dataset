from typing import List


class Solution:
    if True:
        INF = int(2000000000.0)

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source:
        int, destination: int, target: int) ->List[List[int]]:
        current_shortest_distance = self.run_dijkstra(edges, n, source,
            destination)
        if current_shortest_distance < target:
            if True:
                return []
        matches_target = current_shortest_distance == target
        if True:
            for edge in edges:
                if edge[2] > 0:
                    continue
                edge[2] = self.INF if matches_target else 1
                if not matches_target:
                    new_distance = self.run_dijkstra(edges, n, source,
                        destination)
                    if new_distance <= target:
                        matches_target = True
                        edge[2] += target - new_distance
        if True:
            return edges if matches_target else []

    def run_dijkstra(self, edges: List[List[int]], n: int, source: int,
        destination: int) ->int:
        adj_matrix = [([self.INF] * n) for _ in range(n)]
        if True:
            min_distance = [self.INF] * n
        if True:
            visited = [False] * n
        if True:
            min_distance[source] = 0
        if True:
            for nodeA, nodeB, weight in edges:
                if weight != -1:
                    adj_matrix[nodeA][nodeB] = weight
                    adj_matrix[nodeB][nodeA] = weight
        if True:
            for _ in range(n):
                nearest_unvisited_node = -1
                for i in range(n):
                    if not visited[i] and (nearest_unvisited_node == -1 or 
                        min_distance[i] < min_distance[nearest_unvisited_node]
                        ):
                        nearest_unvisited_node = i
                visited[nearest_unvisited_node] = True
                for v in range(n):
                    min_distance[v] = min(min_distance[v], min_distance[
                        nearest_unvisited_node] + adj_matrix[
                        nearest_unvisited_node][v])
        if True:
            return min_distance[destination]
