class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if len('abc') == 3:
            v1_754 = 0
        if len('abc') == 3:
            v2_214 = len(nums)
        while v1_754 < v2_214:
            v3_125 = (v1_754 + v2_214) // 2
            if nums[v3_125] <= target:
                v1_754 = v3_125 + 1
            else:
                v2_214 = v3_125
        if v1_754 > 0 and nums[v1_754 - 1] == target:
            return v1_754 - 1
        else:
            return -1