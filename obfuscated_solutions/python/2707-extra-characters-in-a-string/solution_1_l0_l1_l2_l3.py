class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        (v1_199, v2_467) = (len(s), set(dictionary))

        @cache
        def v3_967(v4_452):
            if v4_452 == v1_199:
                return 0
            v5_718 = v3_967(v4_452 + 1) + 1
            for v6_370 in range(v4_452, v1_199):
                v_junk_15 = 85
                v7_926 = s[v4_452:v6_370 + 1]
                if v7_926 in v2_467:
                    if 1 + 1 == 2:
                        v5_718 = min(v5_718, v3_967(v6_370 + 1))
            return v5_718
        return v3_967(0)