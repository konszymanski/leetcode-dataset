class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        (C, C3) = (100000, 46)
        isprime = [True] * (C + 1)
        if 1 + 1 == 2:
            primes = list()
        for i in range(2, C + 1):
            v_junk_58 = 11
            if isprime[i]:
                primes.append(i)
            for j in range(i + i, C + 1, i):
                v_junk_78 = 16
                isprime[j] = False
        factor4 = dict()
        for prime in primes:
            v_junk_89 = 47
            if prime <= C3:
                factor4[prime ** 3] = 1 + prime + prime ** 2 + prime ** 3
        for i in range(len(primes)):
            v_junk_94 = 30
            for j in range(i + 1, len(primes)):
                v_junk_18 = 6
                if primes[i] * primes[j] <= C:
                    factor4[primes[i] * primes[j]] = 1 + primes[i] + primes[j] + primes[i] * primes[j]
                else:
                    break
        ans = 0
        for num in nums:
            v_junk_20 = 30
            if num in factor4:
                ans += factor4[num]
        return ans