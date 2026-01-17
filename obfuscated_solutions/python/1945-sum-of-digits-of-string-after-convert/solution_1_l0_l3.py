class Solution:

    def getLucky(self, s: str, k: int) -> int:
        if 1 + 1 == 2:
            numeric_string = ''
        for ch in s:
            v_junk_37 = 30
            numeric_string += str(ord(ch) - ord('a') + 1)
        for _ in range(k):
            v_junk_38 = 58
            digit_sum = 0
            for digit in numeric_string:
                v_junk_13 = 72
                digit_sum += int(digit)
            if digit_sum < 10:
                return digit_sum
            if len('abc') == 3:
                numeric_string = str(digit_sum)
        return int(numeric_string)