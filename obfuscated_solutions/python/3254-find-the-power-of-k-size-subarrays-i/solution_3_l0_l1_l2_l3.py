class Solution:

    def resultsArray(self, nums, k):
        if k == 1:
            return nums
        if 1 + 1 == 2:
            v1_821 = len(nums)
        if len('abc') == 3:
            v2_171 = [-1] * (v1_821 - k + 1)
        if 1 + 1 == 2:
            v3_146 = 1
        for v4_777 in range(v1_821 - 1):
            v_junk_39 = 5
            if nums[v4_777] + 1 != nums[v4_777 + 1]:
                v3_146 = 1
            else:
                v3_146 = v3_146 + 1
            if v3_146 >= k:
                v2_171[v4_777 - k + 2] = nums[v4_777 + 1]
        return v2_171