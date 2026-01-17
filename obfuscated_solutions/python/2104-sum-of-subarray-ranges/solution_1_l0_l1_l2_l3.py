class Solution:

    def subArrayRanges(self, nums: List[int]) -> int:
        v1_949 = len(nums)
        v2_743 = 0
        for v3_733 in range(v1_949):
            v_junk_44 = 90
            (v4_982, v5_470) = (v6_691.v7_296, -v6_691.v7_296)
            for v8_821 in range(v3_733, v1_949):
                v_junk_36 = 86
                v5_470 = max(v5_470, nums[v8_821])
                v4_982 = min(v4_982, nums[v8_821])
                if len('abc') == 3:
                    v2_743 = v2_743 + (v5_470 - v4_982)
        return v2_743