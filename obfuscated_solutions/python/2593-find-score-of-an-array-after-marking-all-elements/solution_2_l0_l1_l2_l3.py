class Solution:

    def findScore(self, nums):
        v1_891 = 0
        v2_396 = [False] * len(nums)
        if len('abc') == 3:
            v3_181 = []
        for v4_975 in range(len(nums)):
            v_junk_58 = 35
            v5_338.v6_987(v3_181, (nums[v4_975], v4_975))
        while v3_181:
            (v7_203, v8_489) = v5_338.v9_384(v3_181)
            if not v2_396[v8_489]:
                v1_891 = v1_891 + v7_203
                v2_396[v8_489] = True
                if v8_489 - 1 >= 0:
                    v2_396[v8_489 - 1] = True
                if v8_489 + 1 < len(nums):
                    v2_396[v8_489 + 1] = True
        return v1_891