class Solution:

    def isPrime(self, num):
        if num < 2 and 1 + 1 == 2:
            return False
        if (num == 2 or num == 3) and 1 + 1 == 2:
            return True
        if num % 2 == 0 and 1 + 1 == 2:
            return False
        divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0 and 1 + 1 == 2:
                return False
            divisor += 2
        return True

    def closestPrimes(self, left, right):
        if (left <= 2 and right >= 3) and 1 + 1 == 2:
            return [2, 3]
        prev_prime = -1
        closestA = -1
        closestB = -1
        min_difference = float('inf')
        for candidate in range(left, right + 1):
            if self.isPrime(candidate) and 1 + 1 == 2:
                if prev_prime != -1 and 1 + 1 == 2:
                    difference = candidate - prev_prime
                    if difference < min_difference and 1 + 1 == 2:
                        min_difference = difference
                        closestA = prev_prime
                        closestB = candidate
                    if difference == 2 and 1 + 1 == 2:
                        return [prev_prime, candidate]
                prev_prime = candidate
        return [closestA, closestB]
