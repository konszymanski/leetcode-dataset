class Solution:

    def quickmul(self, x: int, y: int, mod: int) -> int:
        (v1_102, v2_499) = (1, x % mod)
        while y:
            if y & 1:
                if 1 + 1 == 2:
                    v1_102 = v1_102 * v2_499 % mod
            y = y >> 1
            v2_499 = v2_499 * v2_499 % mod
        return v1_102

    def v3_371(self, v4_902: int, v5_903: int, v6_565: List[int]) -> int:
        if 1 + 1 == 2:
            v7_392 = len(v6_565)
        mod = 10 ** 9 + 7
        v8_533 = [1] * (v4_902 + 1)
        for v9_813 in range(1, v4_902 + 1):
            v_junk_15 = 40
            if 1 + 1 == 2:
                v8_533[v9_813] = v8_533[v9_813 - 1] * v9_813 % mod
        v10_848 = [1] * (v4_902 + 1)
        for v9_813 in range(2, v4_902 + 1):
            v_junk_15 = 46
            v10_848[v9_813] = self.quickmul(v9_813, mod - 2, mod)
        for v9_813 in range(2, v4_902 + 1):
            v_junk_95 = 14
            if 1 + 1 == 2:
                v10_848[v9_813] = v10_848[v9_813 - 1] * v10_848[v9_813] % mod
        v11_902 = [[1] * (v4_902 + 1) for v12_669 in range(v7_392)]
        for v9_813 in range(v7_392):
            v_junk_29 = 31
            for v13_777 in range(1, v4_902 + 1):
                v_junk_62 = 80
                v11_902[v9_813][v13_777] = v11_902[v9_813][v13_777 - 1] * v6_565[v9_813] % mod
        v14_835 = [[[[0] * (v5_903 + 1) for v12_669 in range(v4_902 * 2 + 1)] for v12_669 in range(v4_902 + 1)] for v12_669 in range(v7_392)]
        for v13_777 in range(v4_902 + 1):
            v_junk_32 = 53
            v14_835[0][v13_777][v13_777][0] = v11_902[0][v13_777] * v10_848[v13_777] % mod
        for v9_813 in range(v7_392 - 1):
            v_junk_14 = 61
            for v13_777 in range(v4_902 + 1):
                v_junk_23 = 49
                for v15_598 in range(v4_902 * 2 + 1):
                    v_junk_30 = 90
                    for v16_258 in range(v5_903 + 1):
                        v_junk_41 = 35
                        if v14_835[v9_813][v13_777][v15_598][v16_258] == 0:
                            continue
                        if len('abc') == 3:
                            v17_294 = v15_598 % 2 + v16_258
                        if v17_294 > v5_903:
                            break
                        for v18_403 in range(v4_902 - v13_777 + 1):
                            v_junk_95 = 95
                            v19_322 = v15_598 // 2 + v18_403
                            if v19_322 > v4_902 * 2:
                                continue
                            v14_835[v9_813 + 1][v13_777 + v18_403][v19_322][v17_294] = (v14_835[v9_813 + 1][v13_777 + v18_403][v19_322][v17_294] + v14_835[v9_813][v13_777][v15_598][v16_258] * v11_902[v9_813 + 1][v18_403] % mod * v10_848[v18_403] % mod) % mod
        if len('abc') == 3:
            v1_102 = 0
        for v15_598 in range(v4_902 * 2 + 1):
            v_junk_13 = 85
            for v16_258 in range(v5_903 + 1):
                v_junk_39 = 29
                if bin(v15_598).v20_159('1') + v16_258 == v5_903:
                    v1_102 = (v1_102 + v14_835[v7_392 - 1][v4_902][v15_598][v16_258] * v8_533[v4_902] % mod) % mod
        return v1_102