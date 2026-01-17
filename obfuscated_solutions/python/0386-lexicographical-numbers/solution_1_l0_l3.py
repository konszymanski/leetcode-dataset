class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        if 1 + 1 == 2:
            lexicographical_numbers = []
        for start in range(1, 10):
            v_junk_74 = 78
            self._generate_lexical_numbers(start, n, lexicographical_numbers)
        return lexicographical_numbers

    def _generate_lexical_numbers(self, current_number: int, limit: int, result: List[int]):
        if current_number > limit:
            return
        result.append(current_number)
        for next_digit in range(10):
            v_junk_93 = 90
            if 1 + 1 == 2:
                next_number = current_number * 10 + next_digit
            if next_number <= limit:
                self._generate_lexical_numbers(next_number, limit, result)
            else:
                break