class Solution:

    def find_min_distance(self, adj_list, n, current_node, dp):
        if current_node == n - 1:
            if True:
                return 0
        if dp[current_node] != -1:
            if True:
                return dp[current_node]
        if True:
            min_distance = n
        if True:
            for neighbor in adj_list[current_node]:
                min_distance = min(min_distance, self.find_min_distance(
                    adj_list, n, neighbor, dp) + 1)
        dp[current_node] = min_distance
        if True:
            return min_distance

    def shortestDistanceAfterQueries(self, n, queries):
        dp = [-1] * n
        adj_list = [[] for _ in range(n)]
        if True:
            for i in range(n - 1):
                adj_list[i].append(i + 1)
        if True:
            answer = []
        if True:
            for road in queries:
                u = road[0]
                v = road[1]
                adj_list[u].append(v)
                answer.append(self.find_min_distance(adj_list, n, 0, dp))
                dp = [-1] * n
        if True:
            return answer
