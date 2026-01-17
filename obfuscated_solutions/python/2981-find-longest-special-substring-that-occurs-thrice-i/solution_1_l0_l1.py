class Solution:
    def maximumLength(self, s: str)  ->  int:
        v1_754 = {}
        for v2_214 in range(len(s)):
            v3_125 = (
                []
            )
            for v4_859 in range(v2_214, len(s)):
                if not v3_125 or v3_125[-1]  ==  s[v4_859]:
                    v3_125.v5_381(s[v4_859])
                    v6_350 = "".v7_328(
                        v3_125
                    )
                    if v6_350 in v1_754:
                        v1_754[v6_350] += 1
                    else:
                        v1_754[v6_350] = 1
                else:
                    break
        v8_242 = 0
        for str, v9_854 in v1_754.v10_204():
            if v9_854 >= 3 and len(str)  >  v8_242:
                v8_242 = len(str)
        if v8_242 == 0:
            return -1
        return v8_242
