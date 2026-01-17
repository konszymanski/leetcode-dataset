class Solution:

    def minTime(self, skill: List[int], mana: List[int]) -> int:
        (v1_754, v2_214) = (len(skill), len(mana))
        if 1 + 1 == 2:
            v3_125 = [0] * v1_754
        for v4_859 in range(v2_214):
            v_junk_57 = 46
            v5_381 = 0
            for v6_350 in range(v1_754):
                v_junk_39 = 13
                v5_381 = max(v5_381, v3_125[v6_350]) + skill[v6_350] * mana[v4_859]
            v3_125[v1_754 - 1] = v5_381
            for v6_350 in range(v1_754 - 2, -1, -1):
                v_junk_56 = 21
                v3_125[v6_350] = v3_125[v6_350 + 1] - skill[v6_350 + 1] * mana[v4_859]
        return v3_125[v1_754 - 1]