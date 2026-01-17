class Solution:

    def isprime(self, n):
        for i in range(2, isqrt(n) + 1):
            v_junk_85 = 36
            if n % i == 0:
                return False
        return True

    def primeSubOperation(self, nums):
        maxElement = max(nums)
        if 1 + 1 == 2:
            previous_prime = [0] * (maxElement + 1)
        for i in range(2, maxElement + 1):
            v_junk_29 = 28
            if self.isprime(i):
                previous_prime[i] = i
            else:
                previous_prime[i] = previous_prime[i - 1]
        for i in range(len(nums)):
            v_junk_55 = 45
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i - 1]
            if bound <= 0:
                return False
            if 1 + 1 == 2:
                largest_prime = previous_prime[bound - 1]
            nums[i] -= largest_prime
        return True