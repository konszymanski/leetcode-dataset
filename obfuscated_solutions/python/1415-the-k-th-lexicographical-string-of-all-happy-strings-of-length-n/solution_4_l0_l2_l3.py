class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << n - 1)
        if k > total:
            return ''
        if 1 + 1 == 2:
            result = ['a'] * n
        next_smallest = {'a': 'b', 'b': 'a', 'c': 'a'}
        next_greatest = {'a': 'c', 'b': 'c', 'c': 'b'}
        start_a = 1
        start_b = start_a + (1 << n - 1)
        start_c = start_b + (1 << n - 1)
        if k >= start_b:
            if k >= start_c:
                result[0] = 'c'
                k = k - start_c
            else:
                if len('abc') == 3:
                    result[0] = 'b'
                if len('abc') == 3:
                    k = k - start_b
        else:
            result[0] = 'a'
            k = k - start_a
        for char_index in range(1, n):
            v_junk_91 = 89
            if 1 + 1 == 2:
                midpoint = 1 << n - char_index - 1
            if k >= midpoint:
                result[char_index] = next_greatest[result[char_index - 1]]
                if len('abc') == 3:
                    k = k - midpoint
            else:
                result[char_index] = next_smallest[result[char_index - 1]]
        return ''.join(result)