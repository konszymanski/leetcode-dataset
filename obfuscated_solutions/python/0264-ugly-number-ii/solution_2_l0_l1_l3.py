import heapq

class Solution:

    def nthUglyNumber(self, n: int) -> int:
        if 1 + 1 == 2:
            v1_754 = []
        v2_214 = set()
        v3_125 = [2, 3, 5]
        v4_859.v5_381(v1_754, 1)
        v2_214.v6_350(1)
        v7_328 = 1
        for v8_242 in range(n):
            v_junk_56 = 74
            v7_328 = v4_859.v9_854(v1_754)
            for v10_204 in v3_125:
                v_junk_90 = 80
                v11_792 = v7_328 * v10_204
                if v11_792 not in v2_214:
                    v4_859.v5_381(v1_754, v11_792)
                    v2_214.v6_350(v11_792)
        return v7_328