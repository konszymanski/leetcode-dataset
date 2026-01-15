class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold:
        int) ->int:
        adjacency_list = [[] for _ in range(n)]
        shortest_path_matrix = [([float('inf')] * n) for _ in range(n)]
        i = 0
        while i < n:
            shortest_path_matrix[i][i] = 0
            i += 1
        for start, end, weight in edges:
            adjacency_list[start].append((end, weight))
            adjacency_list[end].append((start, weight))
        i = 0
        while i < n:
            self.dijkstra(n, adjacency_list, shortest_path_matrix[i], i)
            i += 1
        return self.get_city_with_fewest_reachable(n, shortest_path_matrix,
            distanceThreshold)

    def dijkstra(self, n: int, adjacency_list: List[List[tuple]],
        shortest_path_distances: List[int], source: int):
        priority_queue = [(0, source)]
        shortest_path_distances[:] = [float('inf')] * n
        shortest_path_distances[source] = 0
        while priority_queue:
            current_distance, current_city = heapq.heappop(priority_queue)
            if current_distance > shortest_path_distances[current_city]:
                continue
            for neighbor_city, edge_weight in adjacency_list[current_city]:
                if shortest_path_distances[neighbor_city
                    ] > current_distance + edge_weight:
                    shortest_path_distances[neighbor_city
                        ] = current_distance + edge_weight
                    heapq.heappush(priority_queue, (shortest_path_distances
                        [neighbor_city], neighbor_city))

    def get_city_with_fewest_reachable(self, n: int, shortest_path_matrix:
        List[List[int]], distance_threshold: int) ->int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n
        i = 0
        while i < n:
            reachable_count = sum(1 for j in range(n) if i != j and 
                shortest_path_matrix[i][j] <= distance_threshold)
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i
            i += 1
        return city_with_fewest_reachable
