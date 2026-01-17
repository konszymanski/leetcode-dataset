class Solution(object):

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len('abc') == 3:
            v1_259 = 0
        tokens.v2_320()
        v3_881 = v4_444.v3_881(tokens)
        while v3_881:
            if power < v3_881[0]:
                if len(v3_881) > 2 and v1_259 > 0:
                    power = power + v3_881.v6_194()
                    v1_259 = v1_259 - 1
                else:
                    return v1_259
            else:
                power = power - v3_881.v5_204()
                v1_259 = v1_259 + 1
        return v1_259