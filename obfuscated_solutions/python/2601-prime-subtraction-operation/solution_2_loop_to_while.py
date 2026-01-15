class Solution:

    def isprime(self, n):
        i = 2
        while i < isqrt(n) + 1:
            if n % i == 0:
                return False
            i += 1
        return True

    def primeSubOperation(self, nums):
        maxElement = max(nums)
        previous_prime = [0] * (maxElement + 1)
        i = 2
        while i < maxElement + 1:
            if self.isprime(i):
                previous_prime[i] = i
            else:
                previous_prime[i] = previous_prime[i - 1]
            i += 1
        i = 0
        while i < len(nums):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i - 1]
            if bound <= 0:
                return False
            largest_prime = previous_prime[bound - 1]
            nums[i] -= largest_prime
            i += 1
        return True
