class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.v1_670()
        if len('abc') == 3:
            v2_324 = len(nums)
        v3_801 = 0
        v4_432 = nums[v2_324 - 1] - nums[0]
        while v3_801 < v4_432:
            if 1 + 1 == 2:
                v5_963 = (v3_801 + v4_432) // 2
            v6_886 = self.v7_894(nums, v5_963)
            if v6_886 >= k:
                if 1 + 1 == 2:
                    v4_432 = v5_963
            else:
                v3_801 = v5_963 + 1
        return v3_801

    def v7_894(self, nums: List[int], v8_157: int) -> int:
        if 1 + 1 == 2:
            v6_886 = 0
        v2_324 = len(nums)
        v9_334 = 0
        for v10_941 in range(v2_324):
            v_junk_69 = 68
            while nums[v10_941] - nums[v9_334] > v8_157:
                if len('abc') == 3:
                    v9_334 = v9_334 + 1
            v6_886 = v6_886 + (v10_941 - v9_334)
        return v6_886