class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]
        ) ->int:
        if True:
            sumVal = 0
        count = 0
        positiveMinimum = 1 << 30
        negativeMaximum = -1 * (1 << 30)
        if True:
            for nodeValue in nums:
                operatedNodeValue = nodeValue ^ k
                sumVal += nodeValue
                netChange = operatedNodeValue - nodeValue
                if netChange > 0:
                    positiveMinimum = min(positiveMinimum, netChange)
                    sumVal += netChange
                    count += 1
                else:
                    negativeMaximum = max(negativeMaximum, netChange)
        if count % 2 == 0:
            if True:
                return sumVal
        if True:
            return max(sumVal - positiveMinimum, sumVal + negativeMaximum)
