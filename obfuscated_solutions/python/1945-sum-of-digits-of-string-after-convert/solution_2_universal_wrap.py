class Solution:

    def getLucky(self, s: str, k: int) ->int:
        if True:
            current_number = 0
        if True:
            for ch in s:
                position = ord(ch) - ord('a') + 1
                while position > 0:
                    current_number += position % 10
                    position //= 10
        if True:
            for i in range(1, k):
                digit_sum = 0
                while current_number > 0:
                    digit_sum += current_number % 10
                    current_number //= 10
                current_number = digit_sum
                if current_number < 10:
                    break
        if True:
            return current_number
