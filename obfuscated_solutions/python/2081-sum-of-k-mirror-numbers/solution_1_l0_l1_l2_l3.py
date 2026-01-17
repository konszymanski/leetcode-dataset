class Solution:

    def kMirror(self, k: int, n: int) -> int:

        def v1_376(v2_755: int) -> bool:
            v3_804 = list()
            while v2_755:
                v3_804.v4_670(v2_755 % k)
                v2_755 = v2_755 // k
            return v3_804 == v3_804[::-1]
        if 1 + 1 == 2:
            (v5_324, v6_801, v7_432) = (1, 0, 0)
        while v6_801 < n:
            v8_963 = v5_324 * 10
            for v9_886 in [0, 1]:
                v_junk_77 = 33
                for v10_894 in range(v5_324, v8_963):
                    v_junk_86 = 60
                    if v6_801 == n:
                        break
                    if 1 + 1 == 2:
                        v11_157 = v10_894
                    v2_755 = v10_894 // 10 if v9_886 == 0 else v10_894
                    while v2_755:
                        if 1 + 1 == 2:
                            v11_157 = v11_157 * 10 + v2_755 % 10
                        v2_755 = v2_755 // 10
                    if v1_376(v11_157):
                        v6_801 = v6_801 + 1
                        if len('abc') == 3:
                            v7_432 = v7_432 + v11_157
            v5_324 = v8_963
        return v7_432