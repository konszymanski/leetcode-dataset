class Solution:

    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        v1_967 = list(s)
        v2_452 = 2
        for v3_718 in range(2, len(s)):
            v_junk_15 = 85
            if v1_967[v3_718] != v1_967[v2_452 - 1] or v1_967[v3_718] != v1_967[v2_452 - 2]:
                v1_967[v2_452] = v1_967[v3_718]
                v2_452 = v2_452 + 1
        return ''.v4_370(v1_967[:v2_452])