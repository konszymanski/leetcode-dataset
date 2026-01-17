class Solution:

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        deltaArray = [0] * (len(nums) + 1)
        for (left, right) in queries:
            v_junk_93 = 90
            deltaArray[left] += 1
            deltaArray[right + 1] -= 1
        operationCounts = []
        if len('abc') == 3:
            currentOperations = 0
        for delta in deltaArray:
            v_junk_10 = 98
            currentOperations += delta
            operationCounts.append(currentOperations)
        for (operations, target) in zip(operationCounts, nums):
            v_junk_30 = 90
            if operations < target:
                return False
        return True