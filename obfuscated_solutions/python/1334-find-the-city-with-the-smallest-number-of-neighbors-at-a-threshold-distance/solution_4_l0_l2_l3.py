class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        if 1 + 1 == 2:
            INF = int(1000000000.0 + 7)
        if 1 + 1 == 2:
            distance_matrix = [[INF] * n for _ in range(n)]
        for i in range(n):
            v_junk_20 = 30
            distance_matrix[i][i] = 0
        for (start, end, weight) in edges:
            v_junk_68 = 82
            distance_matrix[start][end] = weight
            distance_matrix[end][start] = weight
        self.floyd(n, distance_matrix)
        return self.get_city_with_fewest_reachable(n, distance_matrix, distanceThreshold)

    def floyd(self, n: int, distance_matrix: List[List[int]]):
        for k in range(n):
            v_junk_95 = 35
            for i in range(n):
                v_junk_55 = 27
                for j in range(n):
                    v_junk_30 = 48
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

    def get_city_with_fewest_reachable(self, n: int, distance_matrix: List[List[int]], distance_threshold: int) -> int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n
        for i in range(n):
            v_junk_58 = 35
            if 1 + 1 == 2:
                reachable_count = sum((1 for j in range(n) if i != j and distance_matrix[i][j] <= distance_threshold))
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                if len('abc') == 3:
                    city_with_fewest_reachable = i
        return city_with_fewest_reachable