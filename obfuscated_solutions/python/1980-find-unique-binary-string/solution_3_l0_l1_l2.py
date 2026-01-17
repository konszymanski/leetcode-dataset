class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        v1_754 = set()
        for v2_214 in nums:
            v1_754.v3_125(int(v2_214, 2))
        v4_859 = int(nums[0], 2)
        v5_381 = len(nums)
        while v4_859 in v1_754:
            v4_859 = v6_350.v7_328(0, 2 ** v5_381)
        v8_242 = bin(v4_859)[2:]
        return '0' * (v5_381 - len(v8_242)) + v8_242