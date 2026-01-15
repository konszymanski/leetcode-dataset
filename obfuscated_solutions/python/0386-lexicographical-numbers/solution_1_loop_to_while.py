class Solution:

    def lexicalOrder(self, n: int) ->List[int]:
        lexicographical_numbers = []
        start = 1
        while start < 10:
            self._generate_lexical_numbers(start, n, lexicographical_numbers)
            start += 1
        return lexicographical_numbers

    def _generate_lexical_numbers(self, current_number: int, limit: int,
        result: List[int]):
        if current_number > limit:
            return
        result.append(current_number)
        next_digit = 0
        while next_digit < 10:
            next_number = current_number * 10 + next_digit
            if next_number <= limit:
                self._generate_lexical_numbers(next_number, limit, result)
            else:
                break
            next_digit += 1
