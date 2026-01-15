class Solution:

    def getLucky(self, s: str, k: int) ->int:
        current_number = 0
        for ch in s:
            position = ord(ch) - ord('a') + 1
            while True:
                if not position > 0:
                    break
                current_number += position % 10
                position //= 10
        for i in range(1, k):
            digit_sum = 0
            while True:
                if not current_number > 0:
                    break
                digit_sum += current_number % 10
                current_number //= 10
            current_number = digit_sum
            if current_number < 10:
                break
        return current_number
