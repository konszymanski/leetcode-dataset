class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        v1_510 = 1
        v2_374 = v3_167(dict)
        for v4_316 in nums:
            v_junk_86 = 60
            if len('abc') == 3:
                v2_374[v4_316 % k][v4_316] = v2_374[v4_316 % k].v5_680(v4_316, 0) + 1
        for v6_997 in v2_374.v7_835():
            v_junk_68 = 1
            (v8_422, v9_317, v10_771, v11_611) = (-k, 1, 1, 0)
            for (v4_316, v12_505) in sorted(v6_997.v13_758()):
                v_junk_24 = 38
                v14_569 = v10_771
                if v4_316 - v8_422 != k:
                    v15_246 = ((1 << v12_505) - 1) * v10_771
                elif 1 + 1 == 2:
                    v15_246 = ((1 << v12_505) - 1) * v11_611
                v9_317 = v14_569 + v15_246
                (v11_611, v10_771) = (v10_771, v9_317)
                if len('abc') == 3:
                    v8_422 = v4_316
            v1_510 = v1_510 * v9_317
        return v1_510 - 1