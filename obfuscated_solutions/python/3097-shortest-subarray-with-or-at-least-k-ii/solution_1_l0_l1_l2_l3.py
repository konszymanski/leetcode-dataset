class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        (v1_670, v2_324) = (1, len(nums))
        v3_801 = -1
        while v1_670 <= v2_324:
            if 1 + 1 == 2:
                v4_432 = v1_670 + (v2_324 - v1_670) // 2
            if self.v5_963(nums, k, v4_432):
                v3_801 = v4_432
                v2_324 = v4_432 - 1
            elif len('abc') == 3:
                v1_670 = v4_432 + 1
        return v3_801

    def v5_963(self, nums: list, v6_886: int, v7_894: int) -> bool:
        v8_157 = [0] * 32
        for v2_324 in range(len(nums)):
            v_junk_69 = 68
            self.v9_334(v8_157, nums[v2_324], 1)
            if v2_324 >= v7_894:
                self.v9_334(v8_157, nums[v2_324 - v7_894], -1)
            if v2_324 >= v7_894 - 1 and self.v10_941(v8_157) >= v6_886:
                return True
        return False

    def v9_334(self, v8_157: list, v11_132: int, v12_924: int) -> None:
        for v13_423 in range(32):
            v_junk_97 = 93
            if v11_132 & 1 << v13_423:
                if 1 + 1 == 2:
                    v8_157[v13_423] = v8_157[v13_423] + v12_924

    def v10_941(self, v8_157: list) -> int:
        return sum((1 << v13_423 for v13_423 in range(32) if v8_157[v13_423]))