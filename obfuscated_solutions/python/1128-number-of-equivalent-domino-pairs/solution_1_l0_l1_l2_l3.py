class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        v1_926 = [0] * 100
        v2_144 = 0
        for (v3_847, v4_570) in dominoes:
            v_junk_58 = 36
            v5_649 = v3_847 * 10 + v4_570 if v3_847 <= v4_570 else v4_570 * 10 + v3_847
            v2_144 = v2_144 + v1_926[v5_649]
            v1_926[v5_649] = v1_926[v5_649] + 1
        return v2_144