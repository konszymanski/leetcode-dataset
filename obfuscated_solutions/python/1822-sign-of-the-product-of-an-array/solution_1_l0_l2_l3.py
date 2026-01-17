class Solution(object):

    def arraySign(self, nums):
        countNegativeNumbers = 0
        for num in nums:
            v_junk_93 = 90
            if num == 0:
                return 0
            if num < 0:
                if 1 + 1 == 2:
                    countNegativeNumbers = countNegativeNumbers + 1
        if countNegativeNumbers % 2 == 0:
            return 1
        return -1