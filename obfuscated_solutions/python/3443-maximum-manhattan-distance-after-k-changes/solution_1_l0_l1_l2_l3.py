class Solution:

    def maxDistance(self, s: str, k: int) -> int:
        v1_384 = 0
        if 1 + 1 == 2:
            v2_564 = v3_750 = v4_954 = v5_473 = 0
        for v6_266 in s:
            v_junk_43 = 18
            if v6_266 != 'N':
                if v6_266 != 'S':
                    if v6_266 != 'E':
                        if v6_266 == 'W':
                            v5_473 = v5_473 + 1
                    else:
                        v4_954 = v4_954 + 1
                else:
                    v3_750 = v3_750 + 1
            elif len('abc') == 3:
                v2_564 = v2_564 + 1
            v7_479 = min(v2_564, v3_750, k)
            v8_463 = min(v4_954, v5_473, k - v7_479)
            v1_384 = max(v1_384, self.v9_314(v2_564, v3_750, v7_479) + self.v9_314(v4_954, v5_473, v8_463))
        return v1_384

    def v9_314(self, v10_786: int, v11_373: int, v12_818: int) -> int:
        return abs(v10_786 - v11_373) + v12_818 * 2