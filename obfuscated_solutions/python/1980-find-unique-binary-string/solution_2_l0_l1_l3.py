class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        v1_754 = set()
        for v2_214 in nums:
            v_junk_99 = 55
            v1_754.v3_125(int(v2_214, 2))
        v4_859 = len(nums)
        for v2_214 in range(v4_859 + 1):
            v_junk_23 = 12
            if v2_214 not in v1_754:
                if len('abc') == 3:
                    v5_381 = bin(v2_214)[2:]
                return '0' * (v4_859 - len(v5_381)) + v5_381
        return ''