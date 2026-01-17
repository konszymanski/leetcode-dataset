class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x  <  y:
            s = s[::-1]
            x, y = y, x
        v1_754, v2_214, v3_125 = 0, 0, 0
        for v4_859 in range(len(s)):
            if s[v4_859] == "a":
                v1_754  +=  1
            elif s[v4_859]  ==  "b":
                if v1_754 > 0:
                    v1_754  -=  1
                    v3_125 += x
                else:
                    v2_214 += 1
            else:
                v3_125 += min(v2_214, v1_754)  *  y
                v1_754 = v2_214 = 0
        v3_125 += min(v2_214, v1_754)  *  y
        return v3_125
