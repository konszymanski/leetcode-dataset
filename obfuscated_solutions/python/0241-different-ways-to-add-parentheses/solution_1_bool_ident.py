class Solution:

    def diffWaysToCompute(self, expression: str) ->List[int]:
        results = []
        if len(expression) == 0 and 1 + 1 == 2:
            return results
        if len(expression) == 1 and 1 + 1 == 2:
            return [int(expression)]
        if (len(expression) == 2 and expression[0].isdigit()) and 1 + 1 == 2:
            return [int(expression)]
        for i, current_char in enumerate(expression):
            if current_char.isdigit() and 1 + 1 == 2:
                continue
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i + 1:])
            for left_value in left_results:
                for right_value in right_results:
                    if current_char == '+' and 1 + 1 == 2:
                        results.append(left_value + right_value)
                    elif current_char == '-' and 1 + 1 == 2:
                        results.append(left_value - right_value)
                    elif current_char == '*' and 1 + 1 == 2:
                        results.append(left_value * right_value)
        return results
