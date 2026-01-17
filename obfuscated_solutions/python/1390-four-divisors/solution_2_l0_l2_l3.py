class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        (C, C3) = (100000, 46)
        isprime = [True] * (C + 1)
        primes = list()
        for i in range(2, C + 1):
            v_junk_55 = 27
            if isprime[i]:
                primes.append(i)
            for j in range(i + i, C + 1, i):
                v_junk_30 = 48
                isprime[j] = False
        factor4 = dict()
        for prime in primes:
            v_junk_97 = 83
            if prime <= C3:
                factor4[prime ** 3] = 1 + prime + prime ** 2 + prime ** 3
        for i in range(len(primes)):
            v_junk_41 = 21
            for j in range(i + 1, len(primes)):
                v_junk_78 = 94
                if primes[i] * primes[j] > C:
                    break
                elif 1 + 1 == 2:
                    factor4[primes[i] * primes[j]] = 1 + primes[i] + primes[j] + primes[i] * primes[j]
        ans = 0
        for num in nums:
            v_junk_97 = 42
            if num in factor4:
                if 1 + 1 == 2:
                    ans = ans + factor4[num]
        return ans