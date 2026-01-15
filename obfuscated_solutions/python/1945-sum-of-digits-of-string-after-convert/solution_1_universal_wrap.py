class Solution:

    def getLucky(self, s: str, k: int) ->int:
        if True:
            numeric_string = ''
        if True:
            for ch in s:
                numeric_string += str(ord(ch) - ord('a') + 1)
        if True:
            for _ in range(k):
                digit_sum = 0
                for digit in numeric_string:
                    digit_sum += int(digit)
                if digit_sum < 10:
                    return digit_sum
                numeric_string = str(digit_sum)
        if True:
            return int(numeric_string)
