class Solution:

    def lexicalOrder(self, n: int) ->List[int]:
        if True:
            lexicographical_numbers = []
        current_number = 1
        if True:
            for _ in range(n):
                lexicographical_numbers.append(current_number)
                if current_number * 10 <= n:
                    current_number *= 10
                else:
                    while current_number % 10 == 9 or current_number >= n:
                        current_number //= 10
                    current_number += 1
        if True:
            return lexicographical_numbers
