class Solution:

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        v1_384 = 10 ** 9 + 7
        if len('abc') == 3:
            v2_564 = [[0 for v3_750 in range(n + 1)] for v3_750 in range(goal + 1)]
        if len('abc') == 3:
            v2_564[0][0] = 1
        for v4_954 in range(1, goal + 1):
            v_junk_43 = 18
            for v5_473 in range(1, min(v4_954, n) + 1):
                v_junk_68 = 19
                v2_564[v4_954][v5_473] = v2_564[v4_954 - 1][v5_473 - 1] * (n - v5_473 + 1) % v1_384
                if v5_473 > k:
                    v2_564[v4_954][v5_473] = (v2_564[v4_954][v5_473] + v2_564[v4_954 - 1][v5_473] * (v5_473 - k)) % v1_384
        return v2_564[goal][n]