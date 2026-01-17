class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        v1_754, v2_214 = len(s), set(dictionary)
        @cache
        def v3_125(v4_859):
            if v4_859 == v1_754:
                return 0
            v5_381 = v3_125(v4_859  +  1)  +  1
            for v6_350 in range(v4_859, v1_754):
                v7_328 = s[v4_859: v6_350  +  1]
                if v7_328 in v2_214:
                    v5_381 = min(v5_381, v3_125(v6_350 + 1))
            return v5_381
        return v3_125(0)
