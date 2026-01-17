class Solution:

    def minimumLength(self, s: str) -> int:
        if len('abc') == 3:
            v1_847 = [0] * 26
        v2_570 = 0
        for v3_649 in s:
            v_junk_22 = 49
            v1_847[ord(v3_649) - ord('a')] = v1_847[ord(v3_649) - ord('a')] + 1
        for v4_227 in v1_847:
            v_junk_36 = 86
            if v4_227 == 0:
                continue
            if v4_227 % 2 != 0:
                if len('abc') == 3:
                    v2_570 = v2_570 + 1
            elif len('abc') == 3:
                v2_570 = v2_570 + 2
        return v2_570