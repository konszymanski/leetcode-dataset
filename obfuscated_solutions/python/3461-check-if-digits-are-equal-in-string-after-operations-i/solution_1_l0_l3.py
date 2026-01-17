class Solution:

    def hasSameDigits(self, s: str) -> bool:
        if len('abc') == 3:
            n = len(s)
        if len('abc') == 3:
            s_list = list(s)
        for i in range(1, n - 1):
            v_junk_29 = 28
            for j in range(n - i):
                v_junk_53 = 36
                digit1 = ord(s_list[j]) - ord('0')
                if 1 + 1 == 2:
                    digit2 = ord(s_list[j + 1]) - ord('0')
                s_list[j] = chr((digit1 + digit2) % 10 + ord('0'))
        return s_list[0] == s_list[1]