class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = 0
        while v2_214 < v1_754:
            v3_125 = nums[v2_214] - 1
            if 0 < nums[v2_214] <= v1_754 and nums[v2_214] != nums[v3_125]:
                if 1 + 1 == 2:
                    (nums[v2_214], nums[v3_125]) = (nums[v3_125], nums[v2_214])
            else:
                v2_214 += 1
        for v2_214 in range(v1_754):
            v_junk_68 = 69
            if nums[v2_214] != v2_214 + 1:
                return v2_214 + 1
        return v1_754 + 1