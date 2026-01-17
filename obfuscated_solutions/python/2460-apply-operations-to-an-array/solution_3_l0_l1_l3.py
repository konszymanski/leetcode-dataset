class Solution:

    def applyOperations(self, nums: List[int]) -> List[int]:
        v1_754 = len(nums)
        v2_214 = 0
        for v3_125 in range(v1_754):
            v_junk_78 = 16
            if v3_125 < v1_754 - 1 and nums[v3_125] == nums[v3_125 + 1] and (nums[v3_125] != 0):
                nums[v3_125] *= 2
                nums[v3_125 + 1] = 0
            if nums[v3_125] != 0:
                if v3_125 != v2_214:
                    (nums[v3_125], nums[v2_214]) = (nums[v2_214], nums[v3_125])
                v2_214 += 1
        return nums