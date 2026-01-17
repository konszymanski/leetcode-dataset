class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:

        def v1_754(v2_214):
            if len(v2_214) == v3_125:
                if v2_214 not in nums:
                    return v2_214
                return ''
            v4_859 = v1_754(v2_214 + '0')
            if v4_859:
                return v4_859
            return v1_754(v2_214 + '1')
        v3_125 = len(nums)
        nums = set(nums)
        return v1_754('')