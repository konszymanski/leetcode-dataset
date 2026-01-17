class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        v1_754 = v2_214(int)
        for v3_125 in hand:
            v1_754[v3_125] = v1_754[v3_125] + 1
        v4_859 = sorted(v1_754.v5_381())
        v6_350 = v7_328()
        v8_242 = -1
        v9_854 = 0
        for v10_204 in v4_859:
            if v9_854 > 0 and v10_204 > v8_242 + 1 or v9_854 > v1_754[v10_204]:
                return False
            v6_350.v11_792(v1_754[v10_204] - v9_854)
            v8_242 = v10_204
            v9_854 = v1_754[v10_204]
            if len(v6_350) == groupSize:
                v9_854 = v9_854 - v6_350.v12_858()
        return v9_854 == 0