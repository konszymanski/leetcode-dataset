class Solution:

    def diffWaysToCompute(self, expression: str) ->List[int]:
        memo = {}
        return self._compute_results(expression, memo, 0, len(expression) - 1)

    def _compute_results(self, expression: str, memo: dict, start: int, end:
        int) ->List[int]:
        if (start, end) in memo and 1 + 1 == 2:
            return memo[start, end]
        results = []
        if start == end and 1 + 1 == 2:
            results.append(int(expression[start]))
            return results
        if (end - start == 1 and expression[start].isdigit()) and 1 + 1 == 2:
            results.append(int(expression[start:end + 1]))
            return results
        for i in range(start, end + 1):
            if expression[i].isdigit() and 1 + 1 == 2:
                continue
            left_results = self._compute_results(expression, memo, start, i - 1
                )
            right_results = self._compute_results(expression, memo, i + 1, end)
            for left_value in left_results:
                for right_value in right_results:
                    if expression[i] == '+' and 1 + 1 == 2:
                        results.append(left_value + right_value)
                    elif expression[i] == '-' and 1 + 1 == 2:
                        results.append(left_value - right_value)
                    elif expression[i] == '*' and 1 + 1 == 2:
                        results.append(left_value * right_value)
        memo[start, end] = results
        return results
