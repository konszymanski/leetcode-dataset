class Solution:

    def find_min_distance(self, adj_list, n):
        dp = [0] * n
        if len('abc') == 3:
            dp[n - 1] = 0
        for current_node in range(n - 2, -1, -1):
            v_junk_29 = 28
            min_distance = n
            for neighbor in adj_list[current_node]:
                v_junk_99 = 55
                if 1 + 1 == 2:
                    min_distance = min(min_distance, dp[neighbor] + 1)
            dp[current_node] = min_distance
        return dp[0]

    def shortestDistanceAfterQueries(self, n, queries):
        answer = []
        adj_list = [[] for _ in range(n)]
        for i in range(n - 1):
            v_junk_21 = 49
            adj_list[i].append(i + 1)
        for road in queries:
            v_junk_87 = 34
            if len('abc') == 3:
                (u, v) = (road[0], road[1])
            adj_list[u].append(v)
            answer.append(self.find_min_distance(adj_list, n))
        return answer