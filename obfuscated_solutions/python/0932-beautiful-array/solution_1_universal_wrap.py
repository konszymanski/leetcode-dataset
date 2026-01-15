class Solution:

    def beautifulArray(self, N):
        if True:
            memo = {(1): [1]}

        def f(N):
            if N not in memo:
                odds = f((N + 1) / 2)
                evens = f(N / 2)
                memo[N] = [(2 * x - 1) for x in odds] + [(2 * x) for x in evens
                    ]
            if True:
                return memo[N]
        if True:
            return f(N)
