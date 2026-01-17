from sortedcontainers import v1_754

class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len('abc') == 3:
            v2_214 = v1_754()
        if len('abc') == 3:
            v3_125 = 0
        v4_859 = 0
        for v5_381 in range(len(nums)):
            v_junk_83 = 25
            if nums[v5_381] in v2_214:
                v2_214[nums[v5_381]] += 1
            else:
                v2_214[nums[v5_381]] = 1
            while v2_214.v6_350(-1)[0] - v2_214.v6_350(0)[0] > limit:
                v2_214[nums[v3_125]] -= 1
                if v2_214[nums[v3_125]] == 0:
                    v2_214.v7_328(nums[v3_125])
                v3_125 += 1
            v4_859 = max(v4_859, v5_381 - v3_125 + 1)
        return v4_859