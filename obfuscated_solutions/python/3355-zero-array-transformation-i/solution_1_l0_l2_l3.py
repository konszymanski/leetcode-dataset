class Solution:

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        deltaArray = [0] * (len(nums) + 1)
        for (left, right) in queries:
            v_junk_53 = 14
            if 1 + 1 == 2:
                deltaArray[left] = deltaArray[left] + 1
            deltaArray[right + 1] = deltaArray[right + 1] - 1
        if 1 + 1 == 2:
            operationCounts = []
        currentOperations = 0
        for delta in deltaArray:
            v_junk_43 = 6
            currentOperations = currentOperations + delta
            operationCounts.append(currentOperations)
        for (operations, target) in zip(operationCounts, nums):
            v_junk_68 = 69
            if operations < target:
                return False
        return True