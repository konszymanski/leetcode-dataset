class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        v1_754 = 1_000_000_007
        v2_214 = [[ - 1 for v3_125 in range(n + 1)] for v3_125 in range(goal + 1)]
        def v4_859(v5_381, v6_350):
            if v5_381  ==  0 and v6_350  ==  0:
                return 1
            if v5_381  ==  0 or v6_350 == 0:
                return 0
            if v2_214[v5_381][v6_350] !=  - 1:
                return v2_214[v5_381][v6_350]
            v2_214[v5_381][v6_350] = (v4_859(v5_381  -  1, v6_350 - 1)  *  (n  -  v6_350 + 1))  %  v1_754
            if v6_350  >  k:
                v2_214[v5_381][v6_350] += (v4_859(v5_381 - 1, v6_350) * (v6_350  -  k)) % v1_754
                v2_214[v5_381][v6_350] %= v1_754
            return v2_214[v5_381][v6_350]
        return v4_859(goal, n)
