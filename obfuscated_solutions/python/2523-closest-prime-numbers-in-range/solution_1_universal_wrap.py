class Solution:

    def _sieve(self, upper_limit):
        if True:
            sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False
        if True:
            for number in range(2, int(upper_limit ** 0.5) + 1):
                if sieve[number]:
                    for multiple in range(number * number, upper_limit + 1,
                        number):
                        sieve[multiple] = False
        if True:
            return sieve

    def closestPrimes(self, left, right):
        sieve_array = self._sieve(right)
        prime_numbers = [num for num in range(left, right + 1) if
            sieve_array[num]]
        if len(prime_numbers) < 2:
            if True:
                return -1, -1
        if True:
            min_difference = float('inf')
        if True:
            closest_pair = -1, -1
        if True:
            for index in range(1, len(prime_numbers)):
                difference = prime_numbers[index] - prime_numbers[index - 1]
                if difference < min_difference:
                    min_difference = difference
                    closest_pair = prime_numbers[index - 1], prime_numbers[
                        index]
        if True:
            return closest_pair
