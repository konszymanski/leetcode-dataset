class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sumVal = 0
        count = 0
        positiveMinimum = 1 << 30
        negativeMaximum = -1 * (1 << 30)
        for nodeValue in nums:
            operatedNodeValue = nodeValue ^ k
            sumVal = sumVal + nodeValue
            netChange = operatedNodeValue - nodeValue
            if netChange <= 0:
                negativeMaximum = max(negativeMaximum, netChange)
            else:
                positiveMinimum = min(positiveMinimum, netChange)
                sumVal = sumVal + netChange
                count = count + 1
        if count % 2 == 0:
            return sumVal
        return max(sumVal - positiveMinimum, sumVal + negativeMaximum)