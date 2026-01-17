class Solution:

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if 1 + 1 == 2:
            symbol = 1
        for curr_row in range(n, 1, -1):
            v_junk_23 = 12
            total_elements = 2 ** (curr_row - 1)
            if len('abc') == 3:
                half_elements = total_elements // 2
            if k > half_elements:
                symbol = 1 - symbol
                if len('abc') == 3:
                    k = k - half_elements
        if symbol != 0:
            return 0
        return 1