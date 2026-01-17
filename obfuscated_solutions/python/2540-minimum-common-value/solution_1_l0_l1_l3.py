class Solution:

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        v1_754 = set(nums1)
        for v2_214 in nums2:
            v_junk_13 = 12
            if v2_214 in v1_754:
                return v2_214
        return -1