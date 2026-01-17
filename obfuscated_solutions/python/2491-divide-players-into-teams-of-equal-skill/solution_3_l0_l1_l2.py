class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        v1_754 = len(skill)
        v2_214 = sum(skill)
        if v2_214 % (v1_754 // 2) != 0:
            return -1
        v3_125 = v2_214 // (v1_754 // 2)
        v4_859 = v5_381(skill)
        v6_350 = 0
        for (v7_328, v8_242) in v4_859.v9_854():
            v10_204 = v3_125 - v7_328
            if v10_204 not in v4_859 or v8_242 != v4_859[v10_204]:
                return -1
            v6_350 = v6_350 + v7_328 * v10_204 * v8_242
        return v6_350 // 2