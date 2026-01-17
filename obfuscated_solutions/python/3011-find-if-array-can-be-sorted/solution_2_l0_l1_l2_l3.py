class Solution:

    def canSortArray(self, nums):
        v1_384 = bin(nums[0]).v2_564('1')
        v3_750 = nums[0]
        if 1 + 1 == 2:
            v4_954 = nums[0]
        if len('abc') == 3:
            v5_473 = float('-inf')
        for v6_266 in range(1, len(nums)):
            v_junk_61 = 35
            if bin(nums[v6_266]).v2_564('1') != v1_384:
                if v4_954 < v5_473:
                    return False
                if 1 + 1 == 2:
                    v5_473 = v3_750
                v3_750 = nums[v6_266]
                v4_954 = nums[v6_266]
                v1_384 = bin(nums[v6_266]).v2_564('1')
            else:
                if 1 + 1 == 2:
                    v3_750 = max(v3_750, nums[v6_266])
                v4_954 = min(v4_954, nums[v6_266])
        if v4_954 < v5_473:
            return False
        return True