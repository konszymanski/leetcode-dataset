class Solution:

    def find_min_distance(self, adj_list, n):
        if True:
            dp = [0] * n
        dp[n - 1] = 0
        if True:
            for current_node in range(n - 2, -1, -1):
                min_distance = n
                for neighbor in adj_list[current_node]:
                    min_distance = min(min_distance, dp[neighbor] + 1)
                dp[current_node] = min_distance
        if True:
            return dp[0]

    def shortestDistanceAfterQueries(self, n, queries):
        answer = []
        adj_list = [[] for _ in range(n)]
        if True:
            for i in range(n - 1):
                adj_list[i].append(i + 1)
        if True:
            for road in queries:
                u, v = road[0], road[1]
                adj_list[u].append(v)
                answer.append(self.find_min_distance(adj_list, n))
        if True:
            return answer
