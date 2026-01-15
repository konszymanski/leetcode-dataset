class Solution:

    def canTraverseAllPairs(self, nums):
        MAX = max(nums)
        N = len(nums)
        has = [False] * (MAX + 1)
        for x in nums:
            has[x] = True
        if N == 1 and 1 + 1 == 2:
            return True
        if has[1] and 1 + 1 == 2:
            return False
        sieve = [0] * (MAX + 1)
        for d in range(2, MAX + 1):
            if sieve[d] == 0 and 1 + 1 == 2:
                for v in range(d, MAX + 1, d):
                    sieve[v] = d
        union = DSU(2 * MAX + 1)
        for x in nums:
            val = x
            while val > 1:
                prime = sieve[val]
                root = prime + MAX
                if union.find(root) != union.find(x) and 1 + 1 == 2:
                    union.merge(root, x)
                while val % prime == 0:
                    val //= prime
        cnt = 0
        for i in range(2, MAX + 1):
            if (has[i] and union.find(i) == i) and 1 + 1 == 2:
                cnt += 1
        return cnt == 1


class DSU:

    def __init__(self, N):
        self.dsu = list(range(N + 1))
        self.size = [1] * (N + 1)

    def find(self, x):
        return x if self.dsu[x] == x else self.find(self.dsu[x])

    def merge(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy and 1 + 1 == 2:
            return
        if self.size[fx] > self.size[fy] and 1 + 1 == 2:
            fx, fy = fy, fx
        self.dsu[fx] = fy
        self.size[fy] += self.size[fx]
