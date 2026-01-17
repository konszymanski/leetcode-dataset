class Solution:

    def find_min_distance(self, adj_list, n, current_node, dp):
        if current_node == n - 1:
            return 0
        if dp[current_node] != -1:
            return dp[current_node]
        min_distance = n
        for neighbor in adj_list[current_node]:
            min_distance = min(min_distance, self.find_min_distance(adj_list, n, neighbor, dp) + 1)
        dp[current_node] = min_distance
        return min_distance

    def shortestDistanceAfterQueries(self, n, queries):
        dp = [-1] * n
        adj_list = [[] for _ in range(n)]
        for i in range(n - 1):
            adj_list[i].append(i + 1)
        answer = []
        for road in queries:
            u = road[0]
            v = road[1]
            adj_list[u].append(v)
            answer.append(self.find_min_distance(adj_list, n, 0, dp))
            dp = [-1] * n
        return answer