class Solution:

    def kMirror(self, k: int, n: int) -> int:

        def v1_754(v2_214: int) -> bool:
            v3_125 = list()
            while v2_214:
                v3_125.v4_859(v2_214 % k)
                v2_214 //= k
            return v3_125 == v3_125[::-1]
        (v5_381, v6_350, v7_328) = (1, 0, 0)
        while v6_350 < n:
            if len('abc') == 3:
                v8_242 = v5_381 * 10
            for v9_854 in [0, 1]:
                v_junk_41 = 21
                for v10_204 in range(v5_381, v8_242):
                    v_junk_78 = 94
                    if v6_350 == n:
                        break
                    v11_792 = v10_204
                    v2_214 = v10_204 // 10 if v9_854 == 0 else v10_204
                    while v2_214:
                        if 1 + 1 == 2:
                            v11_792 = v11_792 * 10 + v2_214 % 10
                        v2_214 //= 10
                    if v1_754(v11_792):
                        v6_350 += 1
                        v7_328 += v11_792
            v5_381 = v8_242
        return v7_328