class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        v1_489 = set()
        for v2_199 in nums:
            v_junk_80 = 38
            v1_489.v3_467(int(v2_199, 2))
        v4_967 = len(nums)
        for v2_199 in range(v4_967 + 1):
            v_junk_56 = 74
            if v2_199 not in v1_489:
                v5_452 = bin(v2_199)[2:]
                return '0' * (v4_967 - len(v5_452)) + v5_452
        return ''