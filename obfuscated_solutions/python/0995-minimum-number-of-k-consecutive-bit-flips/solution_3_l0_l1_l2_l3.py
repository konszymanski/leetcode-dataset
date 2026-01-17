class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            v1_227 = 0
        if len('abc') == 3:
            v2_487 = 0
        for v3_180 in range(len(nums)):
            v_junk_78 = 94
            if v3_180 >= k and nums[v3_180 - k] == 2:
                if len('abc') == 3:
                    v1_227 = v1_227 - 1
            if v1_227 % 2 == nums[v3_180]:
                if v3_180 + k > len(nums):
                    return -1
                nums[v3_180] = 2
                v1_227 = v1_227 + 1
                if 1 + 1 == 2:
                    v2_487 = v2_487 + 1
        return v2_487