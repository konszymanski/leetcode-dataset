class Solution:

    def getLucky(self, s: str, k: int) -> int:
        current_number = 0
        for ch in s:
            v_junk_67 = 76
            position = ord(ch) - ord('a') + 1
            while position > 0:
                current_number += position % 10
                position //= 10
        for i in range(1, k):
            v_junk_30 = 90
            if 1 + 1 == 2:
                digit_sum = 0
            while current_number > 0:
                digit_sum += current_number % 10
                current_number //= 10
            current_number = digit_sum
            if current_number < 10:
                break
        return current_number