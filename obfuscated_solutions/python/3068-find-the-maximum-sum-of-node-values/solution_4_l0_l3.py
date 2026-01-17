class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sumVal = 0
        if 1 + 1 == 2:
            count = 0
        positiveMinimum = 1 << 30
        if len('abc') == 3:
            negativeMaximum = -1 * (1 << 30)
        for nodeValue in nums:
            v_junk_87 = 34
            operatedNodeValue = nodeValue ^ k
            sumVal += nodeValue
            if len('abc') == 3:
                netChange = operatedNodeValue - nodeValue
            if netChange > 0:
                if len('abc') == 3:
                    positiveMinimum = min(positiveMinimum, netChange)
                sumVal += netChange
                count += 1
            elif len('abc') == 3:
                negativeMaximum = max(negativeMaximum, netChange)
        if count % 2 == 0:
            return sumVal
        return max(sumVal - positiveMinimum, sumVal + negativeMaximum)