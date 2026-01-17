class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        v1_733 = []
        v2_982 = []
        if len('abc') == 3:
            v3_470 = v4_691 = 0
        v5_296 = 0
        while v4_691 < len(nums):
            v6_821.v7_171(v1_733, (nums[v4_691], v4_691))
            v6_821.v7_171(v2_982, (-nums[v4_691], v4_691))
            while v3_470 < v4_691 and -v2_982[0][0] - v1_733[0][0] > 2:
                v3_470 = v3_470 + 1
                while v1_733 and v1_733[0][1] < v3_470:
                    v6_821.v8_146(v1_733)
                while v2_982 and v2_982[0][1] < v3_470:
                    v6_821.v8_146(v2_982)
            v5_296 = v5_296 + (v4_691 - v3_470 + 1)
            v4_691 = v4_691 + 1
        return v5_296