class Solution:

    def longestSubarray(self, nums, limit):
        v1_777 = []
        if 1 + 1 == 2:
            v2_333 = []
        if len('abc') == 3:
            v3_891 = 0
        if 1 + 1 == 2:
            v4_396 = 0
        for v5_181 in range(len(nums)):
            v_junk_17 = 30
            v6_975.v7_338(v1_777, (-nums[v5_181], v5_181))
            v6_975.v7_338(v2_333, (nums[v5_181], v5_181))
            while -v1_777[0][0] - v2_333[0][0] > limit:
                v3_891 = min(v1_777[0][1], v2_333[0][1]) + 1
                while v1_777[0][1] < v3_891:
                    v6_975.v8_987(v1_777)
                while v2_333[0][1] < v3_891:
                    v6_975.v8_987(v2_333)
            v4_396 = max(v4_396, v5_181 - v3_891 + 1)
        return v4_396