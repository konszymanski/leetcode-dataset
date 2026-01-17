class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        v1_754 = 10**9 + 7
        v2_214 = [[0 for v3_125 in range(n  +  1)] for v3_125 in range(goal  +  1)]
        v2_214[0][0] = 1
        for v4_859 in range(1, goal  +  1):
            for v5_381 in range(1, min(v4_859, n) + 1):
                v2_214[v4_859][v5_381] = v2_214[v4_859 - 1][v5_381 - 1]  *  (n  -  v5_381  +  1)  %  v1_754
                if v5_381 > k:
                    v2_214[v4_859][v5_381] = (v2_214[v4_859][v5_381] + v2_214[v4_859 - 1][v5_381]  *  (v5_381  -  k)) % v1_754
        return v2_214[goal][n]
