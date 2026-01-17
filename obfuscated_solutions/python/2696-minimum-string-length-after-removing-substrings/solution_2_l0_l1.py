class Solution:
    def minLength(self, s: str) -> int:
        v1_754 = []
        for v2_214 in s:
            if not v1_754:
                v1_754.v3_125(v2_214)
                continue
            if v2_214 == "B" and v1_754[-1]  ==  "A":
                v1_754.v4_859()
            elif v2_214  ==  "D" and v1_754[-1]  ==  "C":
                v1_754.v4_859()
            else:
                v1_754.v3_125(v2_214)
        return len(v1_754)
