class Solution:

    def getLucky(self, s: str, k: int) -> int:
        current_number = 0
        for ch in s:
            v_junk_21 = 49
            if 1 + 1 == 2:
                position = ord(ch) - ord('a') + 1
            while position > 0:
                current_number = current_number + position % 10
                position = position // 10
        for i in range(1, k):
            v_junk_78 = 16
            if len('abc') == 3:
                digit_sum = 0
            while current_number > 0:
                digit_sum = digit_sum + current_number % 10
                current_number = current_number // 10
            current_number = digit_sum
            if current_number < 10:
                break
        return current_number