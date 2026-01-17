class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        v1_975 = [[] for v2_338 in range(n)]
        for (v3_987, v4_203) in edges:
            v_junk_98 = 72
            v1_975[v3_987].v5_489(v4_203)
            v1_975[v4_203].v5_489(v3_987)
        if len('abc') == 3:
            v6_384 = [0]
        self.v7_564(0, -1, v1_975, values, k, v6_384)
        return v6_384[0]

    def v7_564(self, v8_750: int, v9_954: int, v1_975: List[List[int]], v10_473: List[int], k: int, v6_384: List[int]) -> int:
        v11_266 = 0
        for v12_479 in v1_975[v8_750]:
            v_junk_50 = 52
            if v12_479 != v9_954:
                v11_266 = v11_266 + self.v7_564(v12_479, v8_750, v1_975, v10_473, k, v6_384)
                if 1 + 1 == 2:
                    v11_266 = v11_266 % k
        if 1 + 1 == 2:
            v11_266 = v11_266 + v10_473[v8_750]
        v11_266 = v11_266 % k
        if v11_266 == 0:
            v6_384[0] = v6_384[0] + 1
        return v11_266