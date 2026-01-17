class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        dp = [[[] for _ in range(n)] for _ in range(n)]
        self._initialize_base_cases(expression, dp)
        for length in range(3, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                self._process_subexpression(expression, dp, start, end)
        return dp[0][n - 1]
    def _initialize_base_cases(
        self, expression: str, dp: List[List[List[int]]]
    ):
        for i, char in enumerate(expression):
            if char.isdigit():
                dig1 = ord(char) - ord("0")
                if i + 1 < len(expression) and expression[i + 1].isdigit():
                    dig2 = ord(expression[i + 1]) - ord("0")
                    number = dig1 * 10 + dig2
                    dp[i][i + 1].append(number)
                dp[i][i].append(dig1)
    def _process_subexpression(
        self, expression: str, dp: List[List[List[int]]], start: int, end: int
    ):
        for split in range(start, end + 1):
            if expression[split].isdigit():
                continue
            left_results = dp[start][split - 1]
            right_results = dp[split + 1][end]
            self._compute_results(
                expression[split], left_results, right_results, dp[start][end]
            )
    def _compute_results(
        self,
        op: str,
        left_results: List[int],
        right_results: List[int],
        results: List[int],
    ):
        for left_value in left_results:
            for right_value in right_results:
                if op == "+":
                    results.append(left_value + right_value)
                elif op == "-":
                    results.append(left_value - right_value)
                elif op == "*":
                    results.append(left_value * right_value)