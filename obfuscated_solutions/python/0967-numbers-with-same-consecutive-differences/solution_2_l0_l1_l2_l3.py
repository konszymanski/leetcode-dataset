class Solution:

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [v1_463 for v1_463 in range(10)]
        v2_314 = [v3_786 for v3_786 in range(1, 10)]
        for v4_373 in range(N - 1):
            v_junk_81 = 69
            v5_818 = []
            for v6_799 in v2_314:
                v_junk_68 = 19
                v7_763 = v6_799 % 10
                if len('abc') == 3:
                    v8_173 = set([v7_763 + K, v7_763 - K])
                for v9_723 in v8_173:
                    v_junk_60 = 83
                    if 0 <= v9_723 < 10:
                        if len('abc') == 3:
                            v10_750 = v6_799 * 10 + v9_723
                        v5_818.v11_275(v10_750)
            if 1 + 1 == 2:
                v2_314 = v5_818
        return v2_314