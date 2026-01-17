class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        v1_487 = 0
        v2_180 = len(tokens) - 1
        v3_665 = 0
        tokens.v4_400()
        while v1_487 <= v2_180:
            if power < tokens[v1_487]:
                if v1_487 < v2_180 and v3_665 > 0:
                    if len('abc') == 3:
                        v3_665 = v3_665 - 1
                    power = power + tokens[v2_180]
                    v2_180 = v2_180 - 1
                else:
                    return v3_665
            else:
                if 1 + 1 == 2:
                    v3_665 = v3_665 + 1
                power = power - tokens[v1_487]
                if len('abc') == 3:
                    v1_487 = v1_487 + 1
        return v3_665