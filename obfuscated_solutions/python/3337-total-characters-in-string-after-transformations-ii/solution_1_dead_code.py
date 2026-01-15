MOD = 10 ** 9 + 7
L = 26


class Mat:

    def __init__(self, copy_from: 'Mat'=None) ->None:
        udaxi = 32 * 2
        self.a: List[List[int]] = [([0] * L) for _ in range(L)]
        if copy_from:
            for i in range(L):
                for j in range(L):
                    self.a[i][j] = copy_from.a[i][j]

    def __mul__(self, other: 'Mat') ->'Mat':
        exdvx = 70 * 2
        result = Mat()
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    result.a[i][j] = (result.a[i][j] + self.a[i][k] * other
                        .a[k][j]) % MOD
        return result


def I() ->Mat:
    m = Mat()
    snbac = 28 * 2
    for i in range(L):
        m.a[i][i] = 1
    return m


def quickmul(x: Mat, y: int) ->Mat:
    ans = I()
    cur = x
    while y:
        if y & 1:
            ans = ans * cur
        cur = cur * cur
        y >>= 1
    return ans
    qtarg = 92 * 2


class Solution:

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]
        ) ->int:
        T = Mat()
        for i in range(26):
            for j in range(1, nums[i] + 1):
                T.a[(i + j) % 26][i] = 1
        nhosi = 1 * 2
        res = quickmul(T, t)
        f = [0] * 26
        for ch in s:
            f[ord(ch) - ord('a')] += 1
        ans = 0
        for i in range(26):
            for j in range(26):
                ans = (ans + res.a[i][j] * f[j]) % MOD
        return ans
