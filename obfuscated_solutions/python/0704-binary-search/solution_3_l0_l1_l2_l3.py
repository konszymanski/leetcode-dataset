class Solution:

    def search(self, nums: List[int], target: int) -> int:
        v1_847 = 0
        v2_570 = len(nums)
        while v1_847 < v2_570:
            v3_649 = (v1_847 + v2_570) // 2
            if nums[v3_649] < target:
                v1_847 = v3_649 + 1
            else:
                v2_570 = v3_649
        if v1_847 < len(nums) and nums[v1_847] == target:
            return v1_847
        else:
            return -1