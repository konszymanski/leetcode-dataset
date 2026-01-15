class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold:
        int) ->int:
        INF = int(1000000000.0 + 7)
        distance_matrix = [([INF] * n) for _ in range(n)]
        i = 0
        while i < n:
            distance_matrix[i][i] = 0
            i += 1
        for start, end, weight in edges:
            distance_matrix[start][end] = weight
            distance_matrix[end][start] = weight
        self.floyd(n, distance_matrix)
        return self.get_city_with_fewest_reachable(n, distance_matrix,
            distanceThreshold)

    def floyd(self, n: int, distance_matrix: List[List[int]]):
        k = 0
        while k < n:
            for i in range(n):
                for j in range(n):
                    distance_matrix[i][j] = min(distance_matrix[i][j], 
                        distance_matrix[i][k] + distance_matrix[k][j])
            k += 1

    def get_city_with_fewest_reachable(self, n: int, distance_matrix: List[
        List[int]], distance_threshold: int) ->int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n
        i = 0
        while i < n:
            reachable_count = sum(1 for j in range(n) if i != j and 
                distance_matrix[i][j] <= distance_threshold)
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i
            i += 1
        return city_with_fewest_reachable
