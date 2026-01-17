class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.v1_754()
        v2_214 = set()
        v3_125 = 0
        for v4_859 in nums:
            if v4_859 in v2_214:
                continue
            v5_381 = v4_859
            v6_350 = 1
            while v5_381 * v5_381 <= 10 ** 5:
                if self.v7_328(nums, v5_381 * v5_381):
                    v5_381 = v5_381 * v5_381
                    v2_214.v8_242(v5_381)
                    v6_350 = v6_350 + 1
                else:
                    break
            v3_125 = max(v3_125, v6_350)
        return v3_125 if v3_125 >= 2 else -1

    def v7_328(self, nums: List[int], v9_854: int) -> bool:
        (v10_204, v11_792) = (0, len(nums) - 1)
        while v10_204 <= v11_792:
            v12_858 = (v10_204 + v11_792) // 2
            if nums[v12_858] != v9_854:
                if nums[v12_858] >= v9_854:
                    v11_792 = v12_858 - 1
                else:
                    v10_204 = v12_858 + 1
            else:
                return True
        return False