class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        (v1_754, v2_214) = (len(str1), len(str2))

        def v3_125(v4_859):
            if v1_754 % v4_859 or v2_214 % v4_859:
                return False
            (v5_381, v6_350) = (v1_754 // v4_859, v2_214 // v4_859)
            v7_328 = str1[:v4_859]
            return str1 == v5_381 * v7_328 and str2 == v6_350 * v7_328
        for v8_242 in range(min(v1_754, v2_214), 0, -1):
            if v3_125(v8_242):
                return str1[:v8_242]
        return ''