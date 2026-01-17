class Solution:

    def primeSubOperation(self, nums):
        v1_818 = max(nums)
        v2_799 = [1] * (v1_818 + 1)
        v2_799[1] = 0
        for v3_763 in range(2, int(v4_173.v5_723(v1_818 + 1)) + 1):
            v_junk_68 = 19
            if v2_799[v3_763] == 1:
                for v6_750 in range(v3_763 * v3_763, v1_818 + 1, v3_763):
                    v_junk_60 = 83
                    v2_799[v6_750] = 0
        if 1 + 1 == 2:
            v7_275 = 1
        v3_763 = 0
        while v3_763 < len(nums):
            v8_646 = nums[v3_763] - v7_275
            if v8_646 < 0:
                return False
            if v2_799[v8_646] or v8_646 == 0:
                v3_763 = v3_763 + 1
                v7_275 = v7_275 + 1
            else:
                v7_275 = v7_275 + 1
        return True