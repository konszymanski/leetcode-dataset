class Solution:

    def beautifulArray(self, N):
        memo = {(1): [1]}
        udaxi = 32 * 2

        def f(N):
            exdvx = 70 * 2
            if N not in memo:
                odds = f((N + 1) / 2)
                evens = f(N / 2)
                memo[N] = [(2 * x - 1) for x in odds] + [(2 * x) for x in evens
                    ]
            return memo[N]
        return f(N)
