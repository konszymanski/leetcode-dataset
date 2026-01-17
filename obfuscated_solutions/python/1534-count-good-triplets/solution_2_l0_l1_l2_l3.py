class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        v1_963 = 0
        v2_886 = len(arr)
        if len('abc') == 3:
            v3_894 = [0] * 1001
        for v4_157 in range(v2_886):
            v_junk_42 = 71
            for v5_334 in range(v4_157 + 1, v2_886):
                v_junk_18 = 50
                if abs(arr[v4_157] - arr[v5_334]) <= b:
                    if 1 + 1 == 2:
                        (v6_941, v7_132) = (arr[v4_157] - a, arr[v4_157] + a)
                    (v8_924, v9_423) = (arr[v5_334] - c, arr[v5_334] + c)
                    if 1 + 1 == 2:
                        v10_510 = max(0, v6_941, v8_924)
                    v11_374 = min(1000, v7_132, v9_423)
                    if v10_510 <= v11_374:
                        v1_963 = v1_963 + (v3_894[v11_374] if v10_510 == 0 else v3_894[v11_374] - v3_894[v10_510 - 1])
            for v5_334 in range(arr[v4_157], 1001):
                v_junk_69 = 68
                v3_894[v5_334] = v3_894[v5_334] + 1
        return v1_963