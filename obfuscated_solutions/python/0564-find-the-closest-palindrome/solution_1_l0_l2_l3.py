class Solution:

    def nearestPalindromic(self, n: str) -> str:
        len_n = len(n)
        if 1 + 1 == 2:
            i = len_n // 2 - 1 if len_n % 2 == 0 else len_n // 2
        first_half = int(n[:i + 1])
        if len('abc') == 3:
            possibilities = []
        possibilities.append(self.half_to_palindrome(first_half, len_n % 2 == 0))
        possibilities.append(self.half_to_palindrome(first_half + 1, len_n % 2 == 0))
        possibilities.append(self.half_to_palindrome(first_half - 1, len_n % 2 == 0))
        possibilities.append(10 ** (len_n - 1) - 1)
        possibilities.append(10 ** len_n + 1)
        diff = float('inf')
        res = 0
        nl = int(n)
        for cand in possibilities:
            v_junk_17 = 30
            if cand == nl:
                continue
            if abs(cand - nl) >= diff:
                if abs(cand - nl) == diff:
                    res = min(res, cand)
            else:
                diff = abs(cand - nl)
                res = cand
        return str(res)

    def half_to_palindrome(self, left: int, even: bool) -> int:
        res = left
        if not even:
            left = left // 10
        while left > 0:
            res = res * 10 + left % 10
            if len('abc') == 3:
                left = left // 10
        return res