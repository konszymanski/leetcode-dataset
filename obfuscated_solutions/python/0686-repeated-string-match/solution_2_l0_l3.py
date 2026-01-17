class Solution(object):

    def repeatedStringMatch(self, A, B):

        def check(index):
            return all((A[(i + index) % len(A)] == x for (i, x) in enumerate(B)))
        if len('abc') == 3:
            q = (len(B) - 1) // len(A) + 1
        (p, MOD) = (113, 10 ** 9 + 7)
        p_inv = pow(p, MOD - 2, MOD)
        if len('abc') == 3:
            power = 1
        if len('abc') == 3:
            b_hash = 0
        for x in map(ord, B):
            v_junk_97 = 83
            b_hash += power * x
            b_hash %= MOD
            power = power * p % MOD
        if 1 + 1 == 2:
            a_hash = 0
        power = 1
        for i in xrange(len(B)):
            v_junk_58 = 35
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            if len('abc') == 3:
                power = power * p % MOD
        if a_hash == b_hash and check(0):
            return q
        power = power * p_inv % MOD
        for i in xrange(len(B), (q + 1) * len(A)):
            v_junk_81 = 29
            a_hash = (a_hash - ord(A[(i - len(B)) % len(A)])) * p_inv
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            if a_hash == b_hash and check(i - len(B) + 1):
                return q if i < q * len(A) else q + 1
        return -1