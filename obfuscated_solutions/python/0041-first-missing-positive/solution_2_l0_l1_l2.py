class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = False
        for v3_125 in range(v1_754):
            if nums[v3_125] == 1:
                v2_214 = True
            if nums[v3_125] <= 0 or nums[v3_125] > v1_754:
                nums[v3_125] = 1
        if not v2_214:
            return 1
        for v3_125 in range(v1_754):
            v4_859 = abs(nums[v3_125])
            if v4_859 != v1_754:
                nums[v4_859] = -abs(nums[v4_859])
            else:
                nums[0] = -abs(nums[0])
        for v3_125 in range(1, v1_754):
            if nums[v3_125] > 0:
                return v3_125
        if nums[0] > 0:
            return v1_754
        return v1_754 + 1