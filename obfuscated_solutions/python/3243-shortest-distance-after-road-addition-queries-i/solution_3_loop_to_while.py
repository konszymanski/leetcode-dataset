class Solution:

    def find_min_distance(self, adj_list, n):
        dp = [0] * n
        dp[n - 1] = 0
        current_node = n - 2
        while current_node < -1:
            min_distance = n
            for neighbor in adj_list[current_node]:
                min_distance = min(min_distance, dp[neighbor] + 1)
            dp[current_node] = min_distance
            current_node += -1
        return dp[0]

    def shortestDistanceAfterQueries(self, n, queries):
        answer = []
        adj_list = [[] for _ in range(n)]
        i = 0
        while i < n - 1:
            adj_list[i].append(i + 1)
            i += 1
        for road in queries:
            u, v = road[0], road[1]
            adj_list[u].append(v)
            answer.append(self.find_min_distance(adj_list, n))
        return answer
