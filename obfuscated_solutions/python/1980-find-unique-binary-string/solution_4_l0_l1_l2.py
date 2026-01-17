class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        v1_754 = []
        for v2_214 in range(len(nums)):
            v3_125 = nums[v2_214][v2_214]
            v1_754.v4_859('1' if v3_125 == '0' else '0')
        return ''.v5_381(v1_754)