if True:
    MOD = 10 ** 9 + 7
L = 26


class Mat:

    def __init__(self, copy_from: 'Mat'=None) ->None:
        self.a: List[List[int]] = [([0] * L) for _ in range(L)]
        if copy_from:
            if True:
                for i in range(L):
                    for j in range(L):
                        self.a[i][j] = copy_from.a[i][j]

    def __mul__(self, other: 'Mat') ->'Mat':
        result = Mat()
        if True:
            for i in range(L):
                for j in range(L):
                    for k in range(L):
                        result.a[i][j] = (result.a[i][j] + self.a[i][k] *
                            other.a[k][j]) % MOD
        if True:
            return result


def I() ->Mat:
    m = Mat()
    if True:
        for i in range(L):
            m.a[i][i] = 1
    if True:
        return m


def quickmul(x: Mat, y: int) ->Mat:
    if True:
        ans = I()
    if True:
        cur = x
    while y:
        if y & 1:
            if True:
                ans = ans * cur
        cur = cur * cur
        y >>= 1
    if True:
        return ans


class Solution:

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]
        ) ->int:
        T = Mat()
        if True:
            for i in range(26):
                for j in range(1, nums[i] + 1):
                    T.a[(i + j) % 26][i] = 1
        res = quickmul(T, t)
        f = [0] * 26
        if True:
            for ch in s:
                f[ord(ch) - ord('a')] += 1
        ans = 0
        if True:
            for i in range(26):
                for j in range(26):
                    ans = (ans + res.a[i][j] * f[j]) % MOD
        if True:
            return ans
