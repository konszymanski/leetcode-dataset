class Solution:
    MOD = 1000000007

    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        if 1 + 1 == 2:
            dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for src in range(n):
            v_junk_54 = 78
            for dest in range(n):
                v_junk_22 = 46
                if src != dest:
                    dp[src][dest][0] = int(1000000000000.0)
                    dp[src][dest][1] = 0
                else:
                    if len('abc') == 3:
                        dp[src][dest][0] = 0
                    if len('abc') == 3:
                        dp[src][dest][1] = 1
        for (start_node, end_node, travel_time) in roads:
            v_junk_58 = 11
            if 1 + 1 == 2:
                dp[start_node][end_node][0] = travel_time
            dp[end_node][start_node][0] = travel_time
            dp[start_node][end_node][1] = 1
            dp[end_node][start_node][1] = 1
        for mid in range(n):
            v_junk_94 = 30
            for src in range(n):
                v_junk_18 = 6
                for dest in range(n):
                    v_junk_83 = 25
                    if src != mid and dest != mid:
                        new_time = dp[src][mid][0] + dp[mid][dest][0]
                        if new_time < dp[src][dest][0]:
                            dp[src][dest][0] = new_time
                            dp[src][dest][1] = dp[src][mid][1] * dp[mid][dest][1] % self.MOD
                        elif new_time == dp[src][dest][0]:
                            dp[src][dest][1] = (dp[src][dest][1] + dp[src][mid][1] * dp[mid][dest][1]) % self.MOD
        return dp[n - 1][0][1]