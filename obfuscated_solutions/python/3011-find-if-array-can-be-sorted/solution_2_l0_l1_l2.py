class Solution:

    def canSortArray(self, nums):
        v1_754 = bin(nums[0]).v2_214('1')
        v3_125 = nums[0]
        v4_859 = nums[0]
        v5_381 = float(' - inf')
        for v6_350 in range(1, len(nums)):
            if bin(nums[v6_350]).v2_214('1') != v1_754:
                if v4_859 < v5_381:
                    return False
                v5_381 = v3_125
                v3_125 = nums[v6_350]
                v4_859 = nums[v6_350]
                v1_754 = bin(nums[v6_350]).v2_214('1')
            else:
                v3_125 = max(v3_125, nums[v6_350])
                v4_859 = min(v4_859, nums[v6_350])
        if v4_859 < v5_381:
            return False
        return True