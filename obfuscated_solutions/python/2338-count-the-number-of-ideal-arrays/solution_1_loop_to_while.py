MOD = 10 ** 9 + 7
MAX_N = 10 ** 4 + 10
MAX_P = 15
sieve = [0] * MAX_N
i = 2
while i < MAX_N:
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            sieve[j] = i
    i += 1
ps = [[] for _ in range(MAX_N)]
i = 2
while i < MAX_N:
    x = i
    while x > 1:
        p = sieve[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        ps[i].append(cnt)
    i += 1
c = [([0] * (MAX_P + 1)) for _ in range(MAX_N + MAX_P)]
c[0][0] = 1
i = 1
while i < MAX_N + MAX_P:
    c[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD
    i += 1


class Solution:

    def idealArrays(self, n: int, maxValue: int) ->int:
        ans = 0
        x = 1
        while x < maxValue + 1:
            mul = 1
            for p in ps[x]:
                mul = mul * c[n + p - 1][p] % MOD
            ans = (ans + mul) % MOD
            x += 1
        return ans
