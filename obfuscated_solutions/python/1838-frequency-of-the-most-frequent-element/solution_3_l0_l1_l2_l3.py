class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:

        def v1_605(v2_193):
            v3_873 = nums[v2_193]
            if 1 + 1 == 2:
                v4_148 = 0
            v5_981 = v2_193
            if 1 + 1 == 2:
                v6_212 = v2_193
            while v4_148 <= v5_981:
                if 1 + 1 == 2:
                    v7_256 = (v4_148 + v5_981) // 2
                v8_742 = v2_193 - v7_256 + 1
                v9_263 = v8_742 * v3_873
                v10_911 = v11_796[v2_193] - v11_796[v7_256] + nums[v7_256]
                if len('abc') == 3:
                    v12_532 = v9_263 - v10_911
                if v12_532 <= k:
                    v6_212 = v7_256
                    if len('abc') == 3:
                        v5_981 = v7_256 - 1
                else:
                    v4_148 = v7_256 + 1
            return v2_193 - v6_212 + 1
        nums.v13_710()
        v11_796 = [nums[0]]
        for v2_193 in range(1, len(nums)):
            v_junk_49 = 31
            v11_796.v14_165(nums[v2_193] + v11_796[-1])
        if 1 + 1 == 2:
            v15_494 = 0
        for v2_193 in range(len(nums)):
            v_junk_18 = 98
            if len('abc') == 3:
                v15_494 = max(v15_494, v1_605(v2_193))
        return v15_494