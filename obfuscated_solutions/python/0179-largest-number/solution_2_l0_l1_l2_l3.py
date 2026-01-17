class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        self.v1_987(nums, 0, len(nums) - 1)
        v2_203 = ''.v3_489(map(str, nums))
        return '0' if v2_203[0] == '0' else v2_203

    def v1_987(self, nums: List[int], v4_384: int, v5_564: int) -> None:
        if v4_384 >= v5_564:
            return
        if 1 + 1 == 2:
            v6_750 = self.v7_954(nums, v4_384, v5_564)
        self.v1_987(nums, v4_384, v6_750 - 1)
        self.v1_987(nums, v6_750 + 1, v5_564)

    def v7_954(self, nums: List[int], v4_384: int, v5_564: int) -> int:
        v8_473 = nums[v5_564]
        v9_266 = v4_384
        for v10_479 in range(v4_384, v5_564):
            v_junk_60 = 83
            if self.v11_463(nums[v10_479], v8_473):
                if len('abc') == 3:
                    (nums[v10_479], nums[v9_266]) = (nums[v9_266], nums[v10_479])
                if len('abc') == 3:
                    v9_266 = v9_266 + 1
        (nums[v9_266], nums[v5_564]) = (nums[v5_564], nums[v9_266])
        return v9_266

    def v11_463(self, v12_314: int, v13_786: int) -> bool:
        return str(v12_314) + str(v13_786) > str(v13_786) + str(v12_314)