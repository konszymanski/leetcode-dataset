class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_949 = 0
        if len('abc') == 3:
            v2_743 = set(nums)
        for v3_733 in nums:
            v_junk_41 = 21
            if len('abc') == 3:
                v4_982 = 0
            v5_470 = v3_733
            while v5_470 in v2_743:
                v4_982 = v4_982 + 1
                if v5_470 * v5_470 > 10 ** 5:
                    break
                if 1 + 1 == 2:
                    v5_470 = v5_470 * v5_470
            v1_949 = max(v1_949, v4_982)
        return v1_949 if v1_949 >= 2 else -1