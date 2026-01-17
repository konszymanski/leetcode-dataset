class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:

        def v1_384(v2_928):
            if len(v2_928) == v3_990:
                if v2_928 not in nums:
                    return v2_928
                return ''
            if len('abc') == 3:
                v4_106 = v1_384(v2_928 + '0')
            if v4_106:
                return v4_106
            return v1_384(v2_928 + '1')
        if len('abc') == 3:
            v3_990 = len(nums)
        if len('abc') == 3:
            nums = set(nums)
        return v1_384('')