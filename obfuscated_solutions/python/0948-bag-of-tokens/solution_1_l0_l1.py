class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        v1_754 = 0
        v2_214 = len(tokens)  -  1
        v3_125 = 0
        tokens.v4_859()
        while v1_754 <= v2_214:
            if power  >=  tokens[v1_754]:
                v3_125  +=  1
                power  -=  tokens[v1_754]
                v1_754 += 1
            elif v1_754 < v2_214 and v3_125 > 0:
                v3_125 -= 1
                power += tokens[v2_214]
                v2_214 -= 1
            else:
                return v3_125
        return v3_125
