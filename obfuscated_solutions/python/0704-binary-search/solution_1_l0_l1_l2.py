class Solution:

    def search(self, nums: List[int], target: int) -> int:
        v1_754 = 0
        v2_214 = len(nums) - 1
        while v1_754 <= v2_214:
            v3_125 = (v1_754 + v2_214) // 2
            if nums[v3_125] != target:
                if nums[v3_125] >= target:
                    v2_214 = v3_125 - 1
                else:
                    v1_754 = v3_125 + 1
            else:
                return v3_125
        return -1