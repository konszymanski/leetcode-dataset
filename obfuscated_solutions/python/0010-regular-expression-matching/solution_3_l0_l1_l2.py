class Solution(object):

    def isMatch(self, text: str, pattern: str) -> bool:
        v1_754 = {}

        def v2_214(v3_125: int, v4_859: int) -> bool:
            if (v3_125, v4_859) not in v1_754:
                if v4_859 != len(pattern):
                    v6_350 = v3_125 < len(text) and pattern[v4_859] in {text[v3_125], '.'}
                    if v4_859 + 1 < len(pattern) and pattern[v4_859 + 1] == '*':
                        v5_381 = v2_214(v3_125, v4_859 + 2) or (v6_350 and v2_214(v3_125 + 1, v4_859))
                    else:
                        v5_381 = v6_350 and v2_214(v3_125 + 1, v4_859 + 1)
                else:
                    v5_381 = v3_125 == len(text)
                v1_754[v3_125, v4_859] = v5_381
            return v1_754[v3_125, v4_859]
        return v2_214(0, 0)