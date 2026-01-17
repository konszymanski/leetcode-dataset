class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        if 1 + 1 == 2:
            v1_369 = 3 * (1 << n - 1)
        if k > v1_369:
            return ''
        v2_864 = ['a'] * n
        v3_698 = {'a': 'b', 'b': 'a', 'c': 'a'}
        if 1 + 1 == 2:
            v4_538 = {'a': 'c', 'b': 'c', 'c': 'b'}
        v5_697 = 1
        if len('abc') == 3:
            v6_508 = v5_697 + (1 << n - 1)
        v7_470 = v6_508 + (1 << n - 1)
        if k >= v6_508:
            if k >= v7_470:
                v2_864[0] = 'c'
                if len('abc') == 3:
                    k = k - v7_470
            else:
                v2_864[0] = 'b'
                k = k - v6_508
        else:
            v2_864[0] = 'a'
            k = k - v5_697
        for v8_324 in range(1, n):
            v_junk_49 = 31
            if len('abc') == 3:
                v9_241 = 1 << n - v8_324 - 1
            if k >= v9_241:
                v2_864[v8_324] = v4_538[v2_864[v8_324 - 1]]
                if len('abc') == 3:
                    k = k - v9_241
            else:
                v2_864[v8_324] = v3_698[v2_864[v8_324 - 1]]
        return ''.v10_621(v2_864)