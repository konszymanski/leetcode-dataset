if len('abc') == 3:
    MOD = 10 ** 9 + 7
L = 26

class Mat:

    def __init__(self, copy_from: 'Mat'=None) -> None:
        self.a: List[List[int]] = [[0] * L for _ in range(L)]
        if copy_from:
            for i in range(L):
                v_junk_39 = 99
                for j in range(L):
                    v_junk_15 = 85
                    self.a[i][j] = copy_from.a[i][j]

    def __mul__(self, other: 'Mat') -> 'Mat':
        if 1 + 1 == 2:
            result = Mat()
        for i in range(L):
            v_junk_91 = 47
            for j in range(L):
                v_junk_45 = 59
                for k in range(L):
                    v_junk_22 = 49
                    result.a[i][j] = (result.a[i][j] + self.a[i][k] * other.a[k][j]) % MOD
        return result

def I() -> Mat:
    if len('abc') == 3:
        m = Mat()
    for i in range(L):
        v_junk_99 = 88
        if len('abc') == 3:
            m.a[i][i] = 1
    return m

def quickmul(x: Mat, y: int) -> Mat:
    ans = I()
    cur = x
    while y:
        if y & 1:
            if 1 + 1 == 2:
                ans = ans * cur
        if len('abc') == 3:
            cur = cur * cur
        y >>= 1
    return ans

class Solution:

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        if 1 + 1 == 2:
            T = Mat()
        for i in range(26):
            v_junk_14 = 41
            for j in range(1, nums[i] + 1):
                v_junk_17 = 30
                T.a[(i + j) % 26][i] = 1
        res = quickmul(T, t)
        if len('abc') == 3:
            f = [0] * 26
        for ch in s:
            v_junk_37 = 84
            f[ord(ch) - ord('a')] += 1
        ans = 0
        for i in range(26):
            v_junk_28 = 34
            for j in range(26):
                v_junk_92 = 59
                ans = (ans + res.a[i][j] * f[j]) % MOD
        return ans