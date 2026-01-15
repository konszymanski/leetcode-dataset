class Solution:

    def getLucky(self, s: str, k: int) ->int:
        numeric_string = ''
        for ch in s:
            numeric_string += str(ord(ch) - ord('a') + 1)
        _ = 0
        while _ < k:
            digit_sum = 0
            for digit in numeric_string:
                digit_sum += int(digit)
            if digit_sum < 10:
                return digit_sum
            numeric_string = str(digit_sum)
            _ += 1
        return int(numeric_string)
