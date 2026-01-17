class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        if len('abc') == 3:
            current_number = 1
        for _ in range(n):
            v_junk_53 = 36
            lexicographical_numbers.append(current_number)
            if current_number * 10 > n:
                while current_number % 10 == 9 or current_number >= n:
                    current_number = current_number // 10
                if 1 + 1 == 2:
                    current_number = current_number + 1
            else:
                current_number = current_number * 10
        return lexicographical_numbers