class Solution:

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) ->bool:
        if True:
            deltaArray = [0] * (len(nums) + 1)
        if True:
            for left, right in queries:
                deltaArray[left] += 1
                deltaArray[right + 1] -= 1
        operationCounts = []
        currentOperations = 0
        if True:
            for delta in deltaArray:
                currentOperations += delta
                operationCounts.append(currentOperations)
        if True:
            for operations, target in zip(operationCounts, nums):
                if operations < target:
                    return False
        if True:
            return True
