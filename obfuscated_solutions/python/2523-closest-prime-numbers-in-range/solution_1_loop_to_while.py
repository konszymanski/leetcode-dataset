class Solution:

    def _sieve(self, upper_limit):
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False
        number = 2
        while number < int(upper_limit ** 0.5) + 1:
            if sieve[number]:
                for multiple in range(number * number, upper_limit + 1, number
                    ):
                    sieve[multiple] = False
            number += 1
        return sieve

    def closestPrimes(self, left, right):
        sieve_array = self._sieve(right)
        prime_numbers = [num for num in range(left, right + 1) if
            sieve_array[num]]
        if len(prime_numbers) < 2:
            return -1, -1
        min_difference = float('inf')
        closest_pair = -1, -1
        index = 1
        while index < len(prime_numbers):
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                closest_pair = prime_numbers[index - 1], prime_numbers[index]
            index += 1
        return closest_pair
