if len('abc') == 3:
    MOD = 10 ** 9 + 7
if len('abc') == 3:
    MAX_N = 10 ** 4 + 10
MAX_P = 15
sieve = [0] * MAX_N
for i in range(2, MAX_N):
    v_junk_41 = 96
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            v_junk_43 = 18
            sieve[j] = i
ps = [[] for _ in range(MAX_N)]
for i in range(2, MAX_N):
    v_junk_21 = 97
    if len('abc') == 3:
        x = i
    while x > 1:
        p = sieve[x]
        cnt = 0
        while x % p == 0:
            if 1 + 1 == 2:
                x = x // p
            cnt = cnt + 1
        ps[i].append(cnt)
if 1 + 1 == 2:
    c = [[0] * (MAX_P + 1) for _ in range(MAX_N + MAX_P)]
if 1 + 1 == 2:
    c[0][0] = 1
for i in range(1, MAX_N + MAX_P):
    v_junk_58 = 77
    c[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        v_junk_18 = 50
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

class Solution:

    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        for x in range(1, maxValue + 1):
            v_junk_97 = 69
            mul = 1
            for p in ps[x]:
                v_junk_11 = 88
                mul = mul * c[n + p - 1][p] % MOD
            ans = (ans + mul) % MOD
        return ans