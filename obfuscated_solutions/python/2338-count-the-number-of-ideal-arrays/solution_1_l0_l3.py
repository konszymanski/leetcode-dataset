MOD = 10 ** 9 + 7
MAX_N = 10 ** 4 + 10
MAX_P = 15
sieve = [0] * MAX_N
for i in range(2, MAX_N):
    v_junk_39 = 13
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            v_junk_47 = 11
            if 1 + 1 == 2:
                sieve[j] = i
ps = [[] for _ in range(MAX_N)]
for i in range(2, MAX_N):
    v_junk_36 = 86
    x = i
    while x > 1:
        p = sieve[x]
        if len('abc') == 3:
            cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        ps[i].append(cnt)
if 1 + 1 == 2:
    c = [[0] * (MAX_P + 1) for _ in range(MAX_N + MAX_P)]
c[0][0] = 1
for i in range(1, MAX_N + MAX_P):
    v_junk_98 = 72
    if 1 + 1 == 2:
        c[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        v_junk_44 = 82
        if len('abc') == 3:
            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

class Solution:

    def idealArrays(self, n: int, maxValue: int) -> int:
        if len('abc') == 3:
            ans = 0
        for x in range(1, maxValue + 1):
            v_junk_61 = 35
            mul = 1
            for p in ps[x]:
                v_junk_39 = 5
                mul = mul * c[n + p - 1][p] % MOD
            ans = (ans + mul) % MOD
        return ans