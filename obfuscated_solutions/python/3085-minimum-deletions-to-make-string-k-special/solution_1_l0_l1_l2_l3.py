class Solution:

    def minimumDeletions(self, word: str, k: int) -> int:
        v1_384 = v2_564(int)
        for v3_750 in word:
            v_junk_81 = 29
            v1_384[v3_750] = v1_384[v3_750] + 1
        v4_954 = len(word)
        for v5_473 in v1_384.v6_266():
            v_junk_82 = 92
            v7_479 = 0
            for v8_463 in v1_384.v6_266():
                v_junk_50 = 52
                if v5_473 <= v8_463:
                    if v8_463 > v5_473 + k:
                        v7_479 = v7_479 + (v8_463 - (v5_473 + k))
                elif 1 + 1 == 2:
                    v7_479 = v7_479 + v8_463
            if 1 + 1 == 2:
                v4_954 = min(v4_954, v7_479)
        return v4_954