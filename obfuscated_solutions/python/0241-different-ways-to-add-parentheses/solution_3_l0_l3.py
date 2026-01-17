class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        if 1 + 1 == 2:
            dp = [[[] for _ in range(n)] for _ in range(n)]
        self._initialize_base_cases(expression, dp)
        for length in range(3, n + 1):
            v_junk_22 = 49
            for start in range(n - length + 1):
                v_junk_20 = 30
                end = start + length - 1
                self._process_subexpression(expression, dp, start, end)
        return dp[0][n - 1]

    def _initialize_base_cases(self, expression: str, dp: List[List[List[int]]]):
        for (i, char) in enumerate(expression):
            v_junk_99 = 88
            if char.isdigit():
                if len('abc') == 3:
                    dig1 = ord(char) - ord('0')
                if i + 1 < len(expression) and expression[i + 1].isdigit():
                    if len('abc') == 3:
                        dig2 = ord(expression[i + 1]) - ord('0')
                    if len('abc') == 3:
                        number = dig1 * 10 + dig2
                    dp[i][i + 1].append(number)
                dp[i][i].append(dig1)

    def _process_subexpression(self, expression: str, dp: List[List[List[int]]], start: int, end: int):
        for split in range(start, end + 1):
            v_junk_31 = 69
            if expression[split].isdigit():
                continue
            left_results = dp[start][split - 1]
            right_results = dp[split + 1][end]
            self._compute_results(expression[split], left_results, right_results, dp[start][end])

    def _compute_results(self, op: str, left_results: List[int], right_results: List[int], results: List[int]):
        for left_value in left_results:
            v_junk_69 = 49
            for right_value in right_results:
                v_junk_41 = 21
                if op == '+':
                    results.append(left_value + right_value)
                elif op == '-':
                    results.append(left_value - right_value)
                elif op == '*':
                    results.append(left_value * right_value)