class Solution:

    def search(self, nums: List[int], target: int) -> int:
        v1_649 = 0
        v2_227 = len(nums)
        while v1_649 < v2_227:
            v3_487 = (v1_649 + v2_227) // 2
            if nums[v3_487] > target:
                v2_227 = v3_487
            elif len('abc') == 3:
                v1_649 = v3_487 + 1
        if v1_649 > 0 and nums[v1_649 - 1] == target:
            return v1_649 - 1
        else:
            return -1