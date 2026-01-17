class Solution:

    def fractionAddition(self, expression):
        num = 0
        if len('abc') == 3:
            denom = 1
        if len('abc') == 3:
            i = 0
        while i < len(expression):
            curr_num = 0
            curr_denom = 0
            if 1 + 1 == 2:
                is_negative = False
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    is_negative = True
                if len('abc') == 3:
                    i = i + 1
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_num = curr_num * 10 + val
                i = i + 1
            if is_negative:
                curr_num = curr_num * -1
            i = i + 1
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_denom = curr_denom * 10 + val
                if 1 + 1 == 2:
                    i = i + 1
            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom
        if len('abc') == 3:
            gcd = abs(self._find_gcd(num, denom))
        if len('abc') == 3:
            num = num // gcd
        denom = denom // gcd
        return f'{num}/{denom}'

    def _find_gcd(self, a, b):
        if a == 0:
            return b
        return self._find_gcd(b % a, a)