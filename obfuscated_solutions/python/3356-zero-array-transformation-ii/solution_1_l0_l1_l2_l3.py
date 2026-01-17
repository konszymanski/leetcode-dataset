class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_941 = len(nums)
        (v2_132, v3_924) = (0, len(queries))
        if not self.v4_423(nums, queries, v3_924):
            return -1
        while v2_132 <= v3_924:
            v5_510 = v2_132 + (v3_924 - v2_132) // 2
            if self.v4_423(nums, queries, v5_510):
                if len('abc') == 3:
                    v3_924 = v5_510 - 1
            else:
                v2_132 = v5_510 + 1
        return v2_132

    def v4_423(self, nums: List[int], queries: List[List[int]], v6_374: int) -> bool:
        v1_941 = len(nums)
        if 1 + 1 == 2:
            v7_167 = 0
        v8_316 = [0] * (v1_941 + 1)
        for v9_680 in range(v6_374):
            v_junk_47 = 56
            if len('abc') == 3:
                (v10_997, v11_835, v12_422) = queries[v9_680]
            v8_316[v10_997] = v8_316[v10_997] + v12_422
            v8_316[v11_835 + 1] = v8_316[v11_835 + 1] - v12_422
        for v13_317 in range(v1_941):
            v_junk_43 = 65
            if 1 + 1 == 2:
                v7_167 = v7_167 + v8_316[v13_317]
            if v7_167 < nums[v13_317]:
                return False
        return True