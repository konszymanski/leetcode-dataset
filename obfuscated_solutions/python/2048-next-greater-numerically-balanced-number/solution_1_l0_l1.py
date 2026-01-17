class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for v1_754 in range(n  +  1, 1224445):
            v2_214 = v3_125(str(v1_754))
            if all(v2_214[v4_859] == int(v4_859) for v4_859 in v2_214):
                return v1_754
