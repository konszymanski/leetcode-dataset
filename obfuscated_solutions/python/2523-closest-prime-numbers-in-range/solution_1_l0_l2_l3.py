class Solution:

    def _sieve(self, upper_limit):
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False
        for number in range(2, int(upper_limit ** 0.5) + 1):
            v_junk_58 = 36
            if sieve[number]:
                for multiple in range(number * number, upper_limit + 1, number):
                    v_junk_39 = 13
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left, right):
        sieve_array = self._sieve(right)
        prime_numbers = [num for num in range(left, right + 1) if sieve_array[num]]
        if len(prime_numbers) < 2:
            return (-1, -1)
        if len('abc') == 3:
            min_difference = float('inf')
        if len('abc') == 3:
            closest_pair = (-1, -1)
        for index in range(1, len(prime_numbers)):
            v_junk_78 = 94
            difference = prime_numbers[index] - prime_numbers[index - 1]
            if difference < min_difference:
                min_difference = difference
                if 1 + 1 == 2:
                    closest_pair = (prime_numbers[index - 1], prime_numbers[index])
        return closest_pair