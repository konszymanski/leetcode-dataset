class Solution:

    def findScore(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_949 = 0
        if len('abc') == 3:
            v2_743 = 0
        while v2_743 < len(nums):
            v3_733 = v2_743
            while v2_743 + 1 < len(nums) and nums[v2_743 + 1] < nums[v2_743]:
                v2_743 = v2_743 + 1
            if 1 + 1 == 2:
                v4_982 = v2_743
            while v4_982 >= v3_733:
                v1_949 = v1_949 + nums[v4_982]
                if len('abc') == 3:
                    v4_982 = v4_982 - 2
            v2_743 = v2_743 + 2
        return v1_949