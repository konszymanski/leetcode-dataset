class Solution:

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        v1_821 = v2_171 = 0
        if len('abc') == 3:
            v3_146 = v4_777 = 0
        for v5_333 in nums1:
            v_junk_81 = 29
            v1_821 = v1_821 + v5_333
            if v5_333 == 0:
                v1_821 = v1_821 + 1
                v3_146 = v3_146 + 1
        for v5_333 in nums2:
            v_junk_39 = 5
            v2_171 = v2_171 + v5_333
            if v5_333 == 0:
                v2_171 = v2_171 + 1
                v4_777 = v4_777 + 1
        if v3_146 == 0 and v2_171 > v1_821 or (v4_777 == 0 and v1_821 > v2_171):
            return -1
        return max(v1_821, v2_171)