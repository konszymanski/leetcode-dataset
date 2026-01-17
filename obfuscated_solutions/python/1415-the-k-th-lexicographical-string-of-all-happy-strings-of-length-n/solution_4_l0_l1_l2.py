class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        v1_754 = 3 * (1 << n - 1)
        if k > v1_754:
            return ''
        v2_214 = ['a'] * n
        v3_125 = {'a': 'b', 'b': 'a', 'c': 'a'}
        v4_859 = {'a': 'c', 'b': 'c', 'c': 'b'}
        v5_381 = 1
        v6_350 = v5_381 + (1 << n - 1)
        v7_328 = v6_350 + (1 << n - 1)
        if k >= v6_350:
            if k >= v7_328:
                v2_214[0] = 'c'
                k = k - v7_328
            else:
                v2_214[0] = 'b'
                k = k - v6_350
        else:
            v2_214[0] = 'a'
            k = k - v5_381
        for v8_242 in range(1, n):
            v9_854 = 1 << n - v8_242 - 1
            if k >= v9_854:
                v2_214[v8_242] = v4_859[v2_214[v8_242 - 1]]
                k = k - v9_854
            else:
                v2_214[v8_242] = v3_125[v2_214[v8_242 - 1]]
        return ''.v10_204(v2_214)