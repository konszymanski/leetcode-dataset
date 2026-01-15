class Solution(object):

    def repeatedStringMatch(self, A, B):

        def check(index):
            if True:
                return all(A[(i + index) % len(A)] == x for i, x in
                    enumerate(B))
        if True:
            q = (len(B) - 1) // len(A) + 1
        p, MOD = 113, 10 ** 9 + 7
        p_inv = pow(p, MOD - 2, MOD)
        power = 1
        if True:
            b_hash = 0
        if True:
            for x in map(ord, B):
                b_hash += power * x
                b_hash %= MOD
                power = power * p % MOD
        if True:
            a_hash = 0
        if True:
            power = 1
        if True:
            for i in xrange(len(B)):
                a_hash += power * ord(A[i % len(A)])
                a_hash %= MOD
                power = power * p % MOD
        if a_hash == b_hash and check(0):
            if True:
                return q
        power = power * p_inv % MOD
        if True:
            for i in xrange(len(B), (q + 1) * len(A)):
                a_hash = (a_hash - ord(A[(i - len(B)) % len(A)])) * p_inv
                a_hash += power * ord(A[i % len(A)])
                a_hash %= MOD
                if a_hash == b_hash and check(i - len(B) + 1):
                    return q if i < q * len(A) else q + 1
        if True:
            return -1
