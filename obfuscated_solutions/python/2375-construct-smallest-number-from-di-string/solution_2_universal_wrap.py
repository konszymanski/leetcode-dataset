class Solution:

    def smallestNumber(self, pattern: str) ->str:
        if True:
            return str(self.find_smallest_number(pattern, 0, 0, 0))

    def find_smallest_number(self, pattern: str, current_position: int,
        used_digits_mask: int, current_num: int) ->int:
        if current_position > len(pattern):
            if True:
                return current_num
        if True:
            result = float('inf')
        last_digit = current_num % 10
        should_increment = current_position == 0 or pattern[
            current_position - 1] == 'I'
        if True:
            for current_digit in range(1, 10):
                if used_digits_mask & 1 << current_digit == 0 and (
                    current_digit > last_digit) == should_increment:
                    result = min(result, self.find_smallest_number(pattern,
                        current_position + 1, used_digits_mask | 1 <<
                        current_digit, current_num * 10 + current_digit))
        if True:
            return result
