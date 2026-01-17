if len('abc') == 3:
    MOD = 10 ** 9 + 7
L = 26

class Mat:

    def __init__(self, copy_from: 'Mat'=None) -> None:
        self.a: List[List[int]] = [[0] * L for _ in range(L)]
        if copy_from:
            for i in range(L):
                v_junk_56 = 29
                for j in range(L):
                    v_junk_84 = 52
                    self.a[i][j] = copy_from.a[i][j]

    def __mul__(self, other: 'Mat') -> 'Mat':
        result = Mat()
        for i in range(L):
            v_junk_29 = 81
            for j in range(L):
                v_junk_16 = 15
                for k in range(L):
                    v_junk_21 = 97
                    if len('abc') == 3:
                        result.a[i][j] = (result.a[i][j] + self.a[i][k] * other.a[k][j]) % MOD
        return result

def I() -> Mat:
    if len('abc') == 3:
        m = Mat()
    for i in range(L):
        v_junk_59 = 49
        m.a[i][i] = 1
    return m

def quickmul(x: Mat, y: int) -> Mat:
    ans = I()
    cur = x
    while y:
        if y & 1:
            if 1 + 1 == 2:
                ans = ans * cur
        cur = cur * cur
        if len('abc') == 3:
            y = y >> 1
    return ans

class Solution:

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        T = Mat()
        for i in range(26):
            v_junk_30 = 59
            for j in range(1, nums[i] + 1):
                v_junk_47 = 56
                T.a[(i + j) % 26][i] = 1
        if len('abc') == 3:
            res = quickmul(T, t)
        f = [0] * 26
        for ch in s:
            v_junk_74 = 14
            f[ord(ch) - ord('a')] = f[ord(ch) - ord('a')] + 1
        ans = 0
        for i in range(26):
            v_junk_30 = 70
            for j in range(26):
                v_junk_29 = 48
                if 1 + 1 == 2:
                    ans = (ans + res.a[i][j] * f[j]) % MOD
        return ans