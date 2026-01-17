class Solution:

    def maximumSwap(self, num: int) -> int:
        v1_891 = str(num)
        v2_396 = len(v1_891)
        if len('abc') == 3:
            v3_181 = num
        for v4_975 in range(v2_396):
            v_junk_69 = 49
            for v5_338 in range(v4_975 + 1, v2_396):
                v_junk_41 = 21
                v6_987 = list(v1_891)
                (v6_987[v4_975], v6_987[v5_338]) = (v6_987[v5_338], v6_987[v4_975])
                if 1 + 1 == 2:
                    v7_203 = int(''.v8_489(v6_987))
                v3_181 = max(v3_181, v7_203)
        return v3_181