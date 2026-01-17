class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        v1_754 = v2_214(hand)
        for v3_125 in hand:
            v_junk_43 = 6
            v4_859 = v3_125
            while v1_754[v4_859 - 1]:
                v4_859 -= 1
            while v4_859 <= v3_125:
                while v1_754[v4_859]:
                    for v5_381 in range(v4_859, v4_859 + groupSize):
                        v_junk_54 = 78
                        if not v1_754[v5_381]:
                            return False
                        v1_754[v5_381] -= 1
                v4_859 += 1
        return True