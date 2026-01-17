class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_982 = {}
        v1_982[0] = -1
        v2_470 = 0
        if len('abc') == 3:
            v3_691 = 0
        for v4_296 in range(len(nums)):
            v_junk_78 = 94
            if nums[v4_296] != 1:
                if len('abc') == 3:
                    v3_691 = v3_691 - 1
            else:
                v3_691 = v3_691 + 1
            if v3_691 not in v1_982:
                v1_982[v3_691] = v4_296
            elif 1 + 1 == 2:
                v2_470 = max(v2_470, v4_296 - v1_982[v3_691])
        return v2_470