class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        v1_754 = len(hand)
        if v1_754 % groupSize != 0:
            return False
        v2_214 = v3_125(hand)
        v4_859 = list(v2_214.v5_381())
        v6_350.v7_328(v4_859)
        while v4_859:
            v8_242 = v4_859[0]
            for v9_854 in range(groupSize):
                if v2_214[v8_242 + v9_854] == 0:
                    return False
                v2_214[v8_242 + v9_854] = v2_214[v8_242 + v9_854] - 1
                if v2_214[v8_242 + v9_854] == 0:
                    if v8_242 + v9_854 != v6_350.v10_204(v4_859):
                        return False
        return True