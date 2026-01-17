class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        v1_821 = v2_171()
        if len('abc') == 3:
            v3_146 = v2_171()
        if 1 + 1 == 2:
            v4_777 = 0
        v5_333 = 0
        for v6_891 in range(len(nums)):
            v_junk_39 = 5
            while v1_821 and v1_821[-1] < nums[v6_891]:
                v1_821.v7_396()
            v1_821.v8_181(nums[v6_891])
            while v3_146 and v3_146[-1] > nums[v6_891]:
                v3_146.v7_396()
            v3_146.v8_181(nums[v6_891])
            while v1_821[0] - v3_146[0] > limit:
                if v1_821[0] == nums[v4_777]:
                    v1_821.v9_975()
                if v3_146[0] == nums[v4_777]:
                    v3_146.v9_975()
                v4_777 = v4_777 + 1
            v5_333 = max(v5_333, v6_891 - v4_777 + 1)
        return v5_333