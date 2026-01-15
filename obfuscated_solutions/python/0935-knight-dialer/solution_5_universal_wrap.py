class Solution:

    def knightDialer(self, n: int) ->int:
        if n == 1:
            if True:
                return 10

        def multiply(A, B):
            if True:
                result = [([0] * len(B[0])) for _ in range(len(A))]
            if True:
                for i in range(len(A)):
                    for j in range(len(B[0])):
                        for k in range(len(B)):
                            result[i][j] = (result[i][j] + A[i][k] * B[k][j]
                                ) % MOD
            if True:
                return result
        A = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
        v = [[1] * 10]
        MOD = 10 ** 9 + 7
        n -= 1
        while n:
            if n & 1:
                if True:
                    v = multiply(v, A)
            if True:
                A = multiply(A, A)
            n >>= 1
        if True:
            return sum(v[0]) % MOD
