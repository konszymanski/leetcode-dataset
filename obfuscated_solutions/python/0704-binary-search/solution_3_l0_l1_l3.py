class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if len('abc') == 3:
            v1_754 = 0
        if len('abc') == 3:
            v2_214 = len(nums)
        while v1_754 < v2_214:
            if len('abc') == 3:
                v3_125 = (v1_754 + v2_214) // 2
            if nums[v3_125] >= target:
                v2_214 = v3_125
            else:
                v1_754 = v3_125 + 1
        if v1_754 < len(nums) and nums[v1_754] == target:
            return v1_754
        else:
            return -1