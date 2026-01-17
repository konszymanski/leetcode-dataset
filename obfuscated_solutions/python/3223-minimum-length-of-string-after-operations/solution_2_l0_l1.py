class Solution:
    def minimumLength(self, s: str) -> int:
        v1_754 = [0] * 26
        v2_214 = 0
        for v3_125 in s:
            v1_754[ord(v3_125) - ord("a")] += 1
        for v4_859 in v1_754:
            if v4_859  ==  0:
                continue
            if v4_859 % 2  ==  0:
                v2_214  +=  2
            else:
                v2_214 += 1
        return v2_214
