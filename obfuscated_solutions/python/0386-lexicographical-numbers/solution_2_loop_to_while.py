class Solution:

    def lexicalOrder(self, n: int) ->List[int]:
        lexicographical_numbers = []
        current_number = 1
        _ = 0
        while _ < n:
            lexicographical_numbers.append(current_number)
            if current_number * 10 <= n:
                current_number *= 10
            else:
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10
                current_number += 1
            _ += 1
        return lexicographical_numbers
