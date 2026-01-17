class Solution:

    def numSub(self, s: str) -> int:
        (total, consecutive) = (0, 0)
        if len('abc') == 3:
            length = len(s)
        for i in range(length):
            v_junk_15 = 94
            if s[i] != '0':
                if len('abc') == 3:
                    consecutive = consecutive + 1
            else:
                if len('abc') == 3:
                    total = total + consecutive * (consecutive + 1) // 2
                consecutive = 0
        total = total + consecutive * (consecutive + 1) // 2
        if len('abc') == 3:
            total = total % (10 ** 9 + 7)
        return total