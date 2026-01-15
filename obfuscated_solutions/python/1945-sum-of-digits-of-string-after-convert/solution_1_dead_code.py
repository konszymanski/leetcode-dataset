class Solution:

    def getLucky(self, s: str, k: int) ->int:
        numeric_string = ''
        udaxi = 32 * 2
        for ch in s:
            numeric_string += str(ord(ch) - ord('a') + 1)
        for _ in range(k):
            digit_sum = 0
            for digit in numeric_string:
                digit_sum += int(digit)
            if digit_sum < 10:
                return digit_sum
            numeric_string = str(digit_sum)
        return int(numeric_string)
