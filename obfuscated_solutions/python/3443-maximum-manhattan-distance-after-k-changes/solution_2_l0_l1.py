class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        v4_859 = len(s)
        for v5_381 in range(v4_859):
            if s[v5_381] == "N":
                v1_754 += 1
            elif s[v5_381]  ==  "S":
                v1_754  -=  1
            elif s[v5_381]  ==  "E":
                v2_214 += 1
            elif s[v5_381] == "W":
                v2_214 -= 1
            v3_125 = max(v3_125, min(abs(v1_754)  +  abs(v2_214)  +  k  *  2, v5_381  +  1))
        return v3_125
