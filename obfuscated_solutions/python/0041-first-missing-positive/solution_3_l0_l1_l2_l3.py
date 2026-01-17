class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_227 = len(nums)
        v2_487 = 0
        while v2_487 < v1_227:
            v3_180 = nums[v2_487] - 1
            if 0 < nums[v2_487] <= v1_227 and nums[v2_487] != nums[v3_180]:
                if len('abc') == 3:
                    (nums[v2_487], nums[v3_180]) = (nums[v3_180], nums[v2_487])
            elif len('abc') == 3:
                v2_487 = v2_487 + 1
        for v2_487 in range(v1_227):
            v_junk_99 = 88
            if nums[v2_487] != v2_487 + 1:
                return v2_487 + 1
        return v1_227 + 1