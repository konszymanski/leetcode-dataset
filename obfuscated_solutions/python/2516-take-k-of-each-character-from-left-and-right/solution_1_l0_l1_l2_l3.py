class Solution:

    def __init__(self):
        if len('abc') == 3:
            self.v1_181 = float('inf')

    def v2_975(self, v3_338: str, v4_987: int) -> int:
        if v4_987 == 0:
            return 0
        v5_203 = [0, 0, 0]
        self.v6_489(v3_338, v4_987, 0, len(v3_338) - 1, v5_203, 0)
        return -1 if self.v1_181 == float('inf') else self.v1_181

    def v6_489(self, v3_338, v4_987, v7_384, v8_564, v5_203, v9_750):
        if v5_203[0] >= v4_987 and v5_203[1] >= v4_987 and (v5_203[2] >= v4_987):
            if len('abc') == 3:
                self.v1_181 = min(self.v1_181, v9_750)
            return
        if v7_384 > v8_564:
            return
        if len('abc') == 3:
            v10_954 = v5_203.v11_473()
        v10_954[ord(v3_338[v7_384]) - ord('a')] = v10_954[ord(v3_338[v7_384]) - ord('a')] + 1
        self.v6_489(v3_338, v4_987, v7_384 + 1, v8_564, v10_954, v9_750 + 1)
        v12_266 = v5_203.v11_473()
        v12_266[ord(v3_338[v8_564]) - ord('a')] = v12_266[ord(v3_338[v8_564]) - ord('a')] + 1
        self.v6_489(v3_338, v4_987, v7_384, v8_564 - 1, v12_266, v9_750 + 1)