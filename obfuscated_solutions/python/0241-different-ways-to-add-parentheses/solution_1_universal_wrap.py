class Solution:

    def diffWaysToCompute(self, expression: str) ->List[int]:
        if True:
            results = []
        if len(expression) == 0:
            if True:
                return results
        if len(expression) == 1:
            if True:
                return [int(expression)]
        if len(expression) == 2 and expression[0].isdigit():
            if True:
                return [int(expression)]
        if True:
            for i, current_char in enumerate(expression):
                if current_char.isdigit():
                    continue
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i + 1:])
                for left_value in left_results:
                    for right_value in right_results:
                        if current_char == '+':
                            results.append(left_value + right_value)
                        elif current_char == '-':
                            results.append(left_value - right_value)
                        elif current_char == '*':
                            results.append(left_value * right_value)
        if True:
            return results
