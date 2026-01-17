class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax = (-1, False)
        secondMax = (-1, False)
        thirdMax = (-1, False)
        for num in nums:
            if (firstMax[1] and firstMax[0] == num) or \
                (secondMax[1] and secondMax[0] == num) or \
                (thirdMax[1] and thirdMax[0] == num):
                continue
            if not firstMax[1] or firstMax[0] <= num:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = (num, True)
            elif not secondMax[1] or secondMax[0] <= num:
                thirdMax = secondMax
                secondMax = (num, True)
            elif not thirdMax[1] or thirdMax[0] <= num:
                thirdMax = (num, True)
        if not thirdMax[1]:
            return firstMax[0]
        return thirdMax[0]