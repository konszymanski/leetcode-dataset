class Solution:

    def diffWaysToCompute(self, expression: str) ->List[int]:
        if True:
            memo = {}
        if True:
            return self._compute_results(expression, memo, 0, len(
                expression) - 1)

    def _compute_results(self, expression: str, memo: dict, start: int, end:
        int) ->List[int]:
        if (start, end) in memo:
            if True:
                return memo[start, end]
        results = []
        if start == end:
            results.append(int(expression[start]))
            if True:
                return results
        if end - start == 1 and expression[start].isdigit():
            results.append(int(expression[start:end + 1]))
            if True:
                return results
        if True:
            for i in range(start, end + 1):
                if expression[i].isdigit():
                    continue
                left_results = self._compute_results(expression, memo,
                    start, i - 1)
                right_results = self._compute_results(expression, memo, i +
                    1, end)
                for left_value in left_results:
                    for right_value in right_results:
                        if expression[i] == '+':
                            results.append(left_value + right_value)
                        elif expression[i] == '-':
                            results.append(left_value - right_value)
                        elif expression[i] == '*':
                            results.append(left_value * right_value)
        memo[start, end] = results
        if True:
            return results
