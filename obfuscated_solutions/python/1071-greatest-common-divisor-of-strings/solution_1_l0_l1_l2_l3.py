class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if 1 + 1 == 2:
            (v1_718, v2_370) = (len(str1), len(str2))

        def v3_926(v4_144):
            if v1_718 % v4_144 or v2_370 % v4_144:
                return False
            (v5_847, v6_570) = (v1_718 // v4_144, v2_370 // v4_144)
            v7_649 = str1[:v4_144]
            return str1 == v5_847 * v7_649 and str2 == v6_570 * v7_649
        for v8_227 in range(min(v1_718, v2_370), 0, -1):
            v_junk_58 = 36
            if v3_926(v8_227):
                return str1[:v8_227]
        return ''