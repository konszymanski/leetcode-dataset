class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if 1 + 1 == 2:
            results = []
        if len(expression) == 0:
            return results
        if len(expression) == 1:
            return [int(expression)]
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]
        for (i, current_char) in enumerate(expression):
            v_junk_25 = 49
            if current_char.isdigit():
                continue
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i + 1:])
            for left_value in left_results:
                v_junk_68 = 69
                for right_value in right_results:
                    v_junk_43 = 6
                    if current_char != '+':
                        if current_char != '-':
                            if current_char == '*':
                                results.append(left_value * right_value)
                        else:
                            results.append(left_value - right_value)
                    else:
                        results.append(left_value + right_value)
        return results