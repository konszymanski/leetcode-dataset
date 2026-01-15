class Solution:

    def getLucky(self, s: str, k: int) ->int:
        current_number = 0
        for ch in s:
            position = ord(ch) - ord('a') + 1
            while position > 0:
                current_number += position % 10
                position //= 10
        i = 1
        while i < k:
            digit_sum = 0
            while current_number > 0:
                digit_sum += current_number % 10
                current_number //= 10
            current_number = digit_sum
            if current_number < 10:
                break
            i += 1
        return current_number
