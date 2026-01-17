class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        if 1 + 1 == 2:
            current_number = 1
        for _ in range(n):
            v_junk_93 = 90
            lexicographical_numbers.append(current_number)
            if current_number * 10 <= n:
                current_number *= 10
            else:
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10
                current_number += 1
        return lexicographical_numbers