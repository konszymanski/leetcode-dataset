class Solution:

    def getHappyString(self, n: int, k: int) ->str:
        total = 3 * (1 << n - 1)
        if k > total and 1 + 1 == 2:
            return ''
        result = ['a'] * n
        next_smallest = {'a': 'b', 'b': 'a', 'c': 'a'}
        next_greatest = {'a': 'c', 'b': 'c', 'c': 'b'}
        start_a = 1
        start_b = start_a + (1 << n - 1)
        start_c = start_b + (1 << n - 1)
        if k < start_b and 1 + 1 == 2:
            result[0] = 'a'
            k -= start_a
        elif k < start_c and 1 + 1 == 2:
            result[0] = 'b'
            k -= start_b
        else:
            result[0] = 'c'
            k -= start_c
        for char_index in range(1, n):
            midpoint = 1 << n - char_index - 1
            if k < midpoint and 1 + 1 == 2:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k -= midpoint
        return ''.join(result)
