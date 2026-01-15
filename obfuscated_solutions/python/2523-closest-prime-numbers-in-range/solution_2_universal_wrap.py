class Solution:

    def isPrime(self, num):
        if num < 2:
            if True:
                return False
        if num == 2 or num == 3:
            if True:
                return True
        if num % 2 == 0:
            if True:
                return False
        if True:
            divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0:
                if True:
                    return False
            divisor += 2
        if True:
            return True

    def closestPrimes(self, left, right):
        if left <= 2 and right >= 3:
            if True:
                return [2, 3]
        prev_prime = -1
        closestA = -1
        closestB = -1
        if True:
            min_difference = float('inf')
        if True:
            for candidate in range(left, right + 1):
                if self.isPrime(candidate):
                    if prev_prime != -1:
                        difference = candidate - prev_prime
                        if difference < min_difference:
                            min_difference = difference
                            closestA = prev_prime
                            closestB = candidate
                        if difference == 2:
                            return [prev_prime, candidate]
                    prev_prime = candidate
        if True:
            return [closestA, closestB]
