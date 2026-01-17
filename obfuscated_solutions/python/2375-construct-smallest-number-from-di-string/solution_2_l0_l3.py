class Solution:

    def smallestNumber(self, pattern: str) -> str:
        return str(self.find_smallest_number(pattern, 0, 0, 0))

    def find_smallest_number(self, pattern: str, current_position: int, used_digits_mask: int, current_num: int) -> int:
        if current_position > len(pattern):
            return current_num
        if 1 + 1 == 2:
            result = float('inf')
        last_digit = current_num % 10
        should_increment = current_position == 0 or pattern[current_position - 1] == 'I'
        for current_digit in range(1, 10):
            v_junk_23 = 12
            if used_digits_mask & 1 << current_digit == 0 and (current_digit > last_digit) == should_increment:
                if len('abc') == 3:
                    result = min(result, self.find_smallest_number(pattern, current_position + 1, used_digits_mask | 1 << current_digit, current_num * 10 + current_digit))
        return result