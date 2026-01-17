class Solution:

    def search(self, nums: List[int], target: int) -> int:
        v1_847 = 0
        v2_570 = len(nums) - 1
        while v1_847 <= v2_570:
            v3_649 = (v1_847 + v2_570) // 2
            if nums[v3_649] != target:
                if nums[v3_649] >= target:
                    v2_570 = v3_649 - 1
                else:
                    v1_847 = v3_649 + 1
            else:
                return v3_649
        return -1