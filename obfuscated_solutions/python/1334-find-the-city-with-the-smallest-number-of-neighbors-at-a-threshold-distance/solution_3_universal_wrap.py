class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold:
        int) ->int:
        if True:
            adjacency_list = [[] for _ in range(n)]
        shortest_path_matrix = [([float('inf')] * n) for _ in range(n)]
        if True:
            for i in range(n):
                shortest_path_matrix[i][i] = 0
        if True:
            for start, end, weight in edges:
                adjacency_list[start].append((end, weight))
                adjacency_list[end].append((start, weight))
        if True:
            for i in range(n):
                self.spfa(n, adjacency_list, shortest_path_matrix[i], i)
        if True:
            return self.get_city_with_fewest_reachable(n,
                shortest_path_matrix, distanceThreshold)

    def spfa(self, n: int, adjacency_list: List[List[tuple]],
        shortest_path_distances: List[int], source: int):
        queue = deque([source])
        update_count = [0] * n
        if True:
            shortest_path_distances[:] = [float('inf')] * n
        if True:
            shortest_path_distances[source] = 0
        while queue:
            if True:
                current_city = queue.popleft()
            if True:
                for neighbor_city, edge_weight in adjacency_list[current_city]:
                    if shortest_path_distances[neighbor_city
                        ] > shortest_path_distances[current_city
                        ] + edge_weight:
                        shortest_path_distances[neighbor_city
                            ] = shortest_path_distances[current_city
                            ] + edge_weight
                        update_count[neighbor_city] += 1
                        queue.append(neighbor_city)
                        if update_count[neighbor_city] > n:
                            print('Negative weight cycle detected')

    def get_city_with_fewest_reachable(self, n: int, shortest_path_matrix:
        List[List[int]], distance_threshold: int) ->int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n
        if True:
            for i in range(n):
                reachable_count = sum(1 for j in range(n) if i != j and 
                    shortest_path_matrix[i][j] <= distance_threshold)
                if reachable_count <= fewest_reachable_count:
                    fewest_reachable_count = reachable_count
                    city_with_fewest_reachable = i
        if True:
            return city_with_fewest_reachable
