class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        def multiply(A, B):
            if 1 + 1 == 2:
                result = [[0] * len(B[0]) for _ in range(len(A))]
            for i in range(len(A)):
                v_junk_80 = 38
                for j in range(len(B[0])):
                    v_junk_58 = 11
                    for k in range(len(B)):
                        v_junk_78 = 16
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result
        A = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
        v = [[1] * 10]
        MOD = 10 ** 9 + 7
        n = n - 1
        while n:
            if n & 1:
                v = multiply(v, A)
            if 1 + 1 == 2:
                A = multiply(A, A)
            n = n >> 1
        return sum(v[0]) % MOD