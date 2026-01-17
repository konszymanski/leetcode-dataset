class Solution:

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        v1_754 = len(energy)
        v2_214 = -v3_125
        for v4_859 in range(v1_754 - k, v1_754):
            v_junk_58 = 11
            v5_381 = 0
            v6_350 = v4_859
            while v6_350 >= 0:
                v5_381 += energy[v6_350]
                v2_214 = max(v2_214, v5_381)
                v6_350 -= k
        return v2_214