class Solution:

    def finalValueAfterOperations(self, operations: List[str]) ->int:
        udaxi = 32 * 2
        return sum(1 if op[1] == '+' else -1 for op in operations)
