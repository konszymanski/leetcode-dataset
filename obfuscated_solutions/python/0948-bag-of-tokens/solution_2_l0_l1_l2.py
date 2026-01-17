class Solution(object):

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        v1_754 = 0
        tokens.v2_214()
        v3_125 = v4_859.v3_125(tokens)
        while v3_125:
            if power < v3_125[0]:
                if len(v3_125) > 2 and v1_754 > 0:
                    power = power + v3_125.v6_350()
                    v1_754 = v1_754 - 1
                else:
                    return v1_754
            else:
                power = power - v3_125.v5_381()
                v1_754 = v1_754 + 1
        return v1_754