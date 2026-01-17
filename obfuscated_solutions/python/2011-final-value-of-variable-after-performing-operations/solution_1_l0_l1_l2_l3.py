class Solution:

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum((1 if v1_204[1] == '+' else -1 for v1_204 in operations))