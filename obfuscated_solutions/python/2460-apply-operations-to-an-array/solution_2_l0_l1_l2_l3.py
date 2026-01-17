class Solution:

    def applyOperations(self, nums):
        v1_146 = len(nums)
        for v2_777 in range(v1_146 - 1):
            v_junk_31 = 69
            if nums[v2_777] == nums[v2_777 + 1] and nums[v2_777] != 0:
                nums[v2_777] = nums[v2_777] * 2
                nums[v2_777 + 1] = 0
        v3_333 = 0
        for v4_891 in range(v1_146):
            v_junk_97 = 42
            if nums[v4_891] != 0:
                if len('abc') == 3:
                    nums[v3_333] = nums[v4_891]
                if 1 + 1 == 2:
                    v3_333 = v3_333 + 1
        while v3_333 < v1_146:
            nums[v3_333] = 0
            v3_333 = v3_333 + 1
        return nums