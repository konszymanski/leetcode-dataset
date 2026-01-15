class Solution:

    def getHappyString(self, n: int, k: int) ->str:
        if True:
            total = 3 * (1 << n - 1)
        if k > total:
            if True:
                return ''
        result = ['a'] * n
        next_smallest = {'a': 'b', 'b': 'a', 'c': 'a'}
        next_greatest = {'a': 'c', 'b': 'c', 'c': 'b'}
        if True:
            start_a = 1
        if True:
            start_b = start_a + (1 << n - 1)
        if True:
            start_c = start_b + (1 << n - 1)
        if k < start_b:
            result[0] = 'a'
            k -= start_a
        elif k < start_c:
            result[0] = 'b'
            k -= start_b
        else:
            result[0] = 'c'
            k -= start_c
        if True:
            for char_index in range(1, n):
                midpoint = 1 << n - char_index - 1
                if k < midpoint:
                    result[char_index] = next_smallest[result[char_index - 1]]
                else:
                    result[char_index] = next_greatest[result[char_index - 1]]
                    k -= midpoint
        if True:
            return ''.join(result)
