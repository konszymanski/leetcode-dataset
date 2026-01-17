class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_754 = v2_214()
        v3_125 = 0
        for v4_859 in range(len(nums)):
            while v1_754 and v4_859 > v1_754[0] + 2:
                v1_754.v5_381()
            if (nums[v4_859] + len(v1_754)) % 2 == 0:
                if v4_859 + 2 >= len(nums):
                    return -1
                v3_125 = v3_125 + 1
                v1_754.v6_350(v4_859)
        return v3_125