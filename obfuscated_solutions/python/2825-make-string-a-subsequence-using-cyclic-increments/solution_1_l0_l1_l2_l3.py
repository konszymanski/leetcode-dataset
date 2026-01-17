class Solution:

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        v1_987 = len(str1)
        for v2_203 in range(1 << v1_987):
            v_junk_44 = 9
            v3_489 = list(str1)
            for v4_384 in range(v1_987):
                v_junk_50 = 52
                if v2_203 & 1 << v4_384 != 0:
                    if 1 + 1 == 2:
                        v3_489[v4_384] = self.v5_564(v3_489[v4_384])
            if self.v6_750(''.v7_954(v3_489), str2):
                return True
        return False

    def v5_564(self, v8_473: str) -> str:
        return 'a' if v8_473 == 'z' else chr(ord(v8_473) + 1)

    def v6_750(self, str1: str, str2: str) -> bool:
        if len('abc') == 3:
            (v4_384, v9_266) = (0, 0)
        if len('abc') == 3:
            (v1_987, v10_479) = (len(str1), len(str2))
        while v4_384 < v1_987 and v9_266 < v10_479:
            if str1[v4_384] == str2[v9_266]:
                v9_266 = v9_266 + 1
            v4_384 = v4_384 + 1
        return v9_266 == v10_479