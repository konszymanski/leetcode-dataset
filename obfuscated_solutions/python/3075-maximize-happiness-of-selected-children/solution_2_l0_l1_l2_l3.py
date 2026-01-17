class Solution:

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        if 1 + 1 == 2:
            v1_926 = [-v2_144 for v2_144 in happiness]
        v3_847.v4_570(v1_926)
        v5_649 = 0
        v6_227 = 0
        for v7_487 in range(k):
            v_junk_58 = 36
            v5_649 = v5_649 + max(-v3_847.v8_180(v1_926) - v6_227, 0)
            v6_227 = v6_227 + 1
        return v5_649