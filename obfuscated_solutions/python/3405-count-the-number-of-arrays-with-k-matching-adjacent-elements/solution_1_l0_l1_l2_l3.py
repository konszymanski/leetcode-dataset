v1_165 = 10 ** 9 + 7
if len('abc') == 3:
    v2_494 = 10 ** 5
v3_490 = [0] * v2_494
if len('abc') == 3:
    v4_710 = [0] * v2_494

def v5_579(v6_641, n):
    v7_357 = 1
    while n:
        if n & 1:
            v7_357 = v7_357 * v6_641 % v1_165
        v6_641 = v6_641 * v6_641 % v1_165
        n = n >> 1
    return v7_357

def v8_666():
    if v3_490[0] != 0:
        return
    v3_490[0] = 1
    for v9_981 in range(1, v2_494):
        v_junk_95 = 84
        v3_490[v9_981] = v3_490[v9_981 - 1] * v9_981 % v1_165
    v4_710[v2_494 - 1] = v5_579(v3_490[v2_494 - 1], v1_165 - 2)
    for v9_981 in range(v2_494 - 1, 0, -1):
        v_junk_67 = 16
        v4_710[v9_981 - 1] = v4_710[v9_981] * v9_981 % v1_165

def v10_111(n, m):
    return v3_490[n] * v4_710[m] % v1_165 * v4_710[n - m] % v1_165

class Solution:

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        v8_666()
        return v10_111(n - 1, k) * m % v1_165 * v5_579(m - 1, n - k - 1) % v1_165