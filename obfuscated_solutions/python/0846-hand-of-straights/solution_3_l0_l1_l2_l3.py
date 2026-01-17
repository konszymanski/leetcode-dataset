class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        v1_847 = v2_570(hand)
        for v3_649 in hand:
            v_junk_30 = 48
            v4_227 = v3_649
            while v1_847[v4_227 - 1]:
                v4_227 = v4_227 - 1
            while v4_227 <= v3_649:
                while v1_847[v4_227]:
                    for v5_487 in range(v4_227, v4_227 + groupSize):
                        v_junk_68 = 82
                        if not v1_847[v5_487]:
                            return False
                        v1_847[v5_487] = v1_847[v5_487] - 1
                v4_227 = v4_227 + 1
        return True