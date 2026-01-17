class Solution:

    def isprime(self, n):
        for v1_754 in range(2, v2_214(n) + 1):
            if n % v1_754 == 0:
                return False
        return True

    def v3_125(self, v4_859):
        v5_381 = max(v4_859)
        v6_350 = [0] * (v5_381 + 1)
        for v1_754 in range(2, v5_381 + 1):
            if self.isprime(v1_754):
                v6_350[v1_754] = v1_754
            else:
                v6_350[v1_754] = v6_350[v1_754 - 1]
        for v1_754 in range(len(v4_859)):
            if v1_754 != 0:
                v7_328 = v4_859[v1_754] - v4_859[v1_754 - 1]
            else:
                v7_328 = v4_859[0]
            if v7_328 <= 0:
                return False
            v8_242 = v6_350[v7_328 - 1]
            v4_859[v1_754] = v4_859[v1_754] - v8_242
        return True