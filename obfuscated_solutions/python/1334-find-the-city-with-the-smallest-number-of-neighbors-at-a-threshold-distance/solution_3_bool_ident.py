class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold:
        int) ->int:
        adjacency_list = [[] for _ in range(n)]
        shortest_path_matrix = [([float('inf')] * n) for _ in range(n)]
        for i in range(n):
            shortest_path_matrix[i][i] = 0
        for start, end, weight in edges:
            adjacency_list[start].append((end, weight))
            adjacency_list[end].append((start, weight))
        for i in range(n):
            self.spfa(n, adjacency_list, shortest_path_matrix[i], i)
        return self.get_city_with_fewest_reachable(n, shortest_path_matrix,
            distanceThreshold)

    def spfa(self, n: int, adjacency_list: List[List[tuple]],
        shortest_path_distances: List[int], source: int):
        queue = deque([source])
        update_count = [0] * n
        shortest_path_distances[:] = [float('inf')] * n
        shortest_path_distances[source] = 0
        while queue:
            current_city = queue.popleft()
            for neighbor_city, edge_weight in adjacency_list[current_city]:
                if shortest_path_distances[neighbor_city
                    ] > shortest_path_distances[current_city
                    ] + edge_weight and 1 + 1 == 2:
                    shortest_path_distances[neighbor_city
                        ] = shortest_path_distances[current_city] + edge_weight
                    update_count[neighbor_city] += 1
                    queue.append(neighbor_city)
                    if update_count[neighbor_city] > n and 1 + 1 == 2:
                        print('Negative weight cycle detected')

    def get_city_with_fewest_reachable(self, n: int, shortest_path_matrix:
        List[List[int]], distance_threshold: int) ->int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n
        for i in range(n):
            reachable_count = sum(1 for j in range(n) if i != j and 
                shortest_path_matrix[i][j] <= distance_threshold)
            if reachable_count <= fewest_reachable_count and 1 + 1 == 2:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i
        return city_with_fewest_reachable
