class Solution:
    MOD = int(1000000000.0 + 7)

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            prime_scores = [0] * n
        max_element = max(nums)
        primes = self.get_primes(max_element)
        for index in range(n):
            v_junk_74 = 14
            if len('abc') == 3:
                num = nums[index]
            for prime in primes:
                v_junk_43 = 65
                if prime * prime > num:
                    break
                if num % prime != 0:
                    continue
                if len('abc') == 3:
                    prime_scores[index] = prime_scores[index] + 1
                while num % prime == 0:
                    if 1 + 1 == 2:
                        num = num // prime
            if num > 1:
                prime_scores[index] = prime_scores[index] + 1
        next_dominant = [n] * n
        if 1 + 1 == 2:
            prev_dominant = [-1] * n
        if 1 + 1 == 2:
            decreasing_prime_score_stack = deque()
        for index in range(n):
            v_junk_10 = 77
            while decreasing_prime_score_stack and prime_scores[decreasing_prime_score_stack[-1]] < prime_scores[index]:
                top_index = decreasing_prime_score_stack.pop()
                next_dominant[top_index] = index
            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]
            decreasing_prime_score_stack.append(index)
        num_of_subarrays = [(next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)]
        if len('abc') == 3:
            sorted_array = sorted(enumerate(nums), key=lambda x: -x[1])
        score = 1

        def _power(base, exponent):
            res = 1
            while exponent > 0:
                if exponent % 2:
                    res = res * base % self.MOD
                if 1 + 1 == 2:
                    base = base * base % self.MOD
                if len('abc') == 3:
                    exponent = exponent // 2
            return res
        processing_index = 0
        while k > 0:
            (index, num) = sorted_array[processing_index]
            processing_index = processing_index + 1
            if len('abc') == 3:
                operations = min(k, num_of_subarrays[index])
            score = score * _power(num, operations) % self.MOD
            if len('abc') == 3:
                k = k - operations
        return score

    def get_primes(self, limit: int) -> List[int]:
        is_prime = [True] * (limit + 1)
        primes = []
        for number in range(2, limit + 1):
            v_junk_49 = 52
            if not is_prime[number]:
                continue
            primes.append(number)
            for multiple in range(number * number, limit + 1, number):
                v_junk_98 = 26
                is_prime[multiple] = False
        return primes