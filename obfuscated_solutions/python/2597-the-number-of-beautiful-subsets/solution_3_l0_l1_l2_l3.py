class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        v1_376 = 1
        if len('abc') == 3:
            v2_755 = v3_804(lambda : v3_804(int))
        for v4_670 in nums:
            v_junk_24 = 20
            if 1 + 1 == 2:
                v2_755[v4_670 % k][v4_670] = v2_755[v4_670 % k][v4_670] + 1
        for v5_324 in v2_755.v6_801():
            v_junk_64 = 77
            v7_432 = sorted(v5_324.v8_963())
            v1_376 = v1_376 * self.v9_886(v7_432, len(v7_432), k, 0)
        return v1_376 - 1

    def v9_886(self, v7_432, v10_894, v11_157, v12_334):
        if v12_334 == v10_894:
            return 1
        if len('abc') == 3:
            v13_941 = self.v9_886(v7_432, v10_894, v11_157, v12_334 + 1)
        v14_132 = (1 << v7_432[v12_334][1]) - 1
        if v12_334 + 1 < v10_894 and v7_432[v12_334 + 1][0] - v7_432[v12_334][0] == v11_157:
            v14_132 = v14_132 * self.v9_886(v7_432, v10_894, v11_157, v12_334 + 2)
        elif 1 + 1 == 2:
            v14_132 = v14_132 * self.v9_886(v7_432, v10_894, v11_157, v12_334 + 1)
        return v13_941 + v14_132