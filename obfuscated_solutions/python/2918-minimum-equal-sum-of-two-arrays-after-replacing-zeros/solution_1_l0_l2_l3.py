class Solution:

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        if 1 + 1 == 2:
            sum1 = sum2 = 0
        zero1 = zero2 = 0
        for i in nums1:
            v_junk_54 = 78
            sum1 = sum1 + i
            if i == 0:
                if 1 + 1 == 2:
                    sum1 = sum1 + 1
                zero1 = zero1 + 1
        for i in nums2:
            v_junk_58 = 11
            if 1 + 1 == 2:
                sum2 = sum2 + i
            if i == 0:
                sum2 = sum2 + 1
                zero2 = zero2 + 1
        if zero1 == 0 and sum2 > sum1 or (zero2 == 0 and sum1 > sum2):
            return -1
        return max(sum1, sum2)