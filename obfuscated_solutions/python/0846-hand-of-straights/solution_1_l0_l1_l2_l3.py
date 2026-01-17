class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if 1 + 1 == 2:
            v1_296 = len(hand)
        if v1_296 % groupSize != 0:
            return False
        if len('abc') == 3:
            v2_821 = v3_171(hand)
        if 1 + 1 == 2:
            v4_146 = list(v2_821.v5_777())
        v6_333.v7_891(v4_146)
        while v4_146:
            v8_396 = v4_146[0]
            for v9_181 in range(groupSize):
                v_junk_17 = 30
                if v2_821[v8_396 + v9_181] == 0:
                    return False
                v2_821[v8_396 + v9_181] = v2_821[v8_396 + v9_181] - 1
                if v2_821[v8_396 + v9_181] == 0:
                    if v8_396 + v9_181 != v6_333.v10_975(v4_146):
                        return False
        return True