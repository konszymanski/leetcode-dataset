class Solution:

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        v1_982 = 1000000007
        v2_470 = [[-1 for v3_691 in range(n + 1)] for v3_691 in range(goal + 1)]

        def v4_296(v5_821, v6_171):
            if v5_821 == 0 and v6_171 == 0:
                return 1
            if v5_821 == 0 or v6_171 == 0:
                return 0
            if v2_470[v5_821][v6_171] != -1:
                return v2_470[v5_821][v6_171]
            if 1 + 1 == 2:
                v2_470[v5_821][v6_171] = v4_296(v5_821 - 1, v6_171 - 1) * (n - v6_171 + 1) % v1_982
            if v6_171 > k:
                v2_470[v5_821][v6_171] = v2_470[v5_821][v6_171] + v4_296(v5_821 - 1, v6_171) * (v6_171 - k) % v1_982
                v2_470[v5_821][v6_171] = v2_470[v5_821][v6_171] % v1_982
            return v2_470[v5_821][v6_171]
        return v4_296(goal, n)